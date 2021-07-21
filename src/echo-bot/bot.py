# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing_extensions import IntVar
from botbuilder.core import ActivityHandler, TurnContext, CardFactory, MessageFactory
from botbuilder.schema import ChannelAccount
from todo_errors import NoSlashError, InvalidCommandError
from card_maker import cardMaker
from datetime import datetime

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    def __init__(self, task_manager=None, time=None):
        self.task_manager = task_manager
        ActivityHandler.__init__(self)
        self.today = self.generateDate(datetime.utcnow())

    async def on_message_activity(self, turn_context: TurnContext):
        title = ""
        text = ""
        type = ""
        user_id = turn_context.activity.recipient.id
        msg = ""
        try:
            title,text,type = self.task_manager.handleCommand(turn_context.activity.text, user_id, self.today)
            if type is not None:
                card = cardMaker().makeCard(title, text, type)
                msg = MessageFactory.attachment(CardFactory.hero_card(card))
        
        except InvalidCommandError as ex:
            msg = f"'{ex.command}'{ex.message}"
            await turn_context.send_activity(msg)

        except NoSlashError as e:
            msg = e.message
            await turn_context.send_activity(msg)
        
        except Exception as e:
            msg = "Something went wrong: " + e.message
            await turn_context.send_activity(msg)

        finally:
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
                await turn_context.send_activity("Good morning, StandUpBuddy here! If you're looking for help using StandUpBuddy, see a list of available commands, use '/help'!")
    
    def generateDate(self, time):
        full_date = time.strftime("%d-%b-%Y (%H:%M:%S.%f)") #18-Nov-2018 (08:34:58.674035)
        date = full_date.split(" ")
        date = date[0]
        return date 
    
# date = MyBot.generateDate(MyBot().time) 
    # if (date[:2] == date[:1]): 
    #     turn_context.send_activity("Good morning, StandUpBuddy here! Today is Wednesday July 21st, 2021. If you're looking for help using StandUpBuddy, see a list of available commands, use '/help'!")

    