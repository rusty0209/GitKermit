# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing_extensions import IntVar
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
from todo_errors import NoSlashError, InvalidCommandError


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    def __init__(self, task_manager):
        self.task_manager = task_manager
        ActivityHandler.__init__(self)

    async def on_message_activity(self, turn_context: TurnContext):
        show = False
        try:
            msg = self.task_manager.handleCommand(turn_context.activity.text, user_id)
            print(msg)
            if msg[0:5] == "show":
                show = True
        except InvalidCommandError as e:
            msg = f"'{e.command}'{e.message}"
            await turn_context.send_activity(msg)

        except NoSlashError as e:
            msg = e.message
            await turn_context.send_activity(msg)

        if show:
            for i in msg[0:5].split("\n"):
                await turn_context.send_activity(msg)

        await turn_context.send_activity(msg)
        #await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                global user_id
                user_id = turn_context.activity.recipient.id
                await turn_context.send_activity("Hello and welcome!")
