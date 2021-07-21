# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing_extensions import IntVar
from botbuilder.core import ActivityHandler, TurnContext, CardFactory, MessageFactory
from botbuilder.schema import ChannelAccount
from todo_errors import NoSlashError, InvalidCommandError
from card_maker import cardMaker


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    def __init__(self, task_manager):
        self.task_manager = task_manager
        ActivityHandler.__init__(self)

    async def on_message_activity(self, turn_context: TurnContext):
        title = ""
        text = ""
        try:
            title,text = self.task_manager.handleCommand(turn_context.activity.text, user_id)
          
        except InvalidCommandError as ex:
            msg = f"'{ex.command}'{ex.message}"
            await turn_context.send_activity(msg)

        except NoSlashError as e:
            msg = e.message
            await turn_context.send_activity(msg)

        finally:
            card = cardMaker().cardmaker(title, text)
            await turn_context.send_activity(MessageFactory.attachment(CardFactory.hero_card(card)))
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
                await turn_context.send_activity("Hello! To see a list of available commands, use '/help'!")
