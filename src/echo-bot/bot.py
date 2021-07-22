# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing_extensions import IntVar
from botbuilder.core import ActivityHandler, TurnContext, CardFactory, MessageFactory
from botbuilder.schema import ChannelAccount
from todo_errors import NoSlashError, InvalidCommandError
from card_maker import cardMaker
from datetime import datetime, timedelta
from CONSTANTS import *

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    def __init__(self, task_manager=None, time=None):
        self.task_manager = task_manager
        ActivityHandler.__init__(self)
        self.utc = datetime.utcnow()

    async def on_message_activity(self, turn_context: TurnContext):
        title = ""
        text = ""
        type = ""
        user_id = turn_context.activity.recipient.id
        msg = ""
        if turn_context.activity.text:
            if "/tomorrow" in turn_context.activity.text:
                self.addDay()
                # date = self.generateDate(self.utc)[0]
                # time = self.generateDate(self.utc)[1]
                # WELCOMETITLE = f"Good morning, StandUpBuddy here! \n\n Today is {date}. It's {time}."
                # card = cardMaker().makeCard(WELCOMETITLE, WELCOMEMSG, "welcome")
                # msg = MessageFactory.attachment(CardFactory.hero_card(card))
                # await turn_context.send_activity(msg)
            try:
                title,text,type = self.task_manager.handleCommand(turn_context.activity.text, user_id, self.utc)
                if type is not None:
                    card = cardMaker().makeCard(title, text, type)
                    msg = MessageFactory.attachment(CardFactory.hero_card(card))
                    await turn_context.send_activity(msg)
            
            
            except InvalidCommandError as ex:
                msg = f"'{ex.command}'{ex.message}"
                await turn_context.send_activity(msg)

            except NoSlashError as e:
                msg = e.message
                await turn_context.send_activity(msg)
            
            except Exception as e:
                error = "Error message not found."
                if hasattr(e, "message"):
                    error = e.message
                msg = "Something went wrong: " + error
                await turn_context.send_activity(msg)

                

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                global user_id
                user_id = turn_context.activity.recipient.id
                date = self.generateDate(self.utc)[0]
                time = self.generateDate(self.utc)[1]
                WELCOMETITLE = f"Good evening, StandUpBuddy here! \n\n  Today is {date}. It's {time} UTC."
                card = cardMaker().makeCard(WELCOMETITLE, WELCOMEMSG, "welcome")
                msg = MessageFactory.attachment(CardFactory.hero_card(card))
                await turn_context.send_activity(msg)
    
    def generateDate(self, utc):
        """returns string of date"""
        full_date = utc.strftime("%d-%b-%Y (%H:%M:%S.%f)") #18-Nov-2018 (08:34:58.674035)
        print(full_date)
        date = full_date.split(" ")[0] #18-Nov-2018
        time_stamp = full_date.split(" ")[1]
        time = time_stamp[1:6]
        date = date.split("-") #(18, Nov, 2018))
        return f"{date[1]} {date[0]}, {date[2]}", time

    def addDay(self):
        self.nineAM()
        self.utc = self.utc + timedelta(days=+1)

    def nineAM(self):
        """ 
        sets time to 9:00 AM 
        """
        now = self.utc
        year = int(now.strftime("%Y"))
        month = int(now.strftime("%m"))
        day = int(now.strftime("%d")) 
        self.utc = datetime(year, month, day, 9, 00)
        print(datetime(year, month, day, 9, 00))
        print(self.generateDate(datetime(year, month, day, 9, 00)))
        return

    