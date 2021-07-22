from botbuilder.core import (
    ActivityHandler,
    TurnContext,
    UserState,
    CardFactory,
    MessageFactory,
)
from botbuilder.schema import (
    ChannelAccount,
    HeroCard,
    CardImage,
    CardAction,
    ActionTypes,
)
from isodate.isodates import build_date_regexps


class cardMaker(): 
    def makeCard(self, title, text, type):
        if type == "todo":
            return self.toDoCard(title,text, False)
        elif type == "todopriorityset":
            return self.toDoCard(title,text, True)
        elif type == "complete":
            return self.completeCard(title,text)
        elif type == "tomorrow":
            return self.tomorrowCard(title, text)
        elif type == "are you sure":
            return self.areYouSureCard(title, text)
        elif type == "welcome":
            return self.welcomeCard(title, text)
        elif type == "standup":
            return self.standupCard(title, text)
        elif type == "spelling":
            return self.spellingCard(title, text)
        elif type in ["edit", "description", "status", "priority", "clear", "remove", "show", "help"]:
            return self.genericCard(title, text)
    
    
    def spellingCard(self, title, text):
        # User misspelled a command, suggest closest match (pic: confused standupbot)
        card = HeroCard(
            title=title,
            text=text,
            images=[CardImage(url="https://i.ibb.co/tLZ8FKw/2.png")]
        )
        return card

    def welcomeCard(self, title, text):
        # User misspelled a command, suggest closest match (pic: confused standupbot)
        card = HeroCard(
            title=title,
            text=text,
            images=[CardImage(url="https://i.ibb.co/4KZ69DF/welcome.png")],
            buttons=[   
                CardAction(
                    type=ActionTypes.message_back,
                    title="9:30",
                    value="9:30",
                ),
                CardAction(
                    type=ActionTypes.message_back,
                    title="10:00",
                    value="10:00",
                ),
                CardAction(
                    type=ActionTypes.message_back,
                    title="10:30",
                    value="10:30",
                ),
                CardAction(
                    type=ActionTypes.message_back,
                    title="11:00",
                    value="11:00",
                ),CardAction(
                    type=ActionTypes.message_back,
                    title="11:30",
                    value="11:30",
                )
            ]
        )
        return card
    
    def genericCard(self, title, text):
        # no need for img here
        card = HeroCard(
            title=title,
            text=text,
            #images=[CardImage(url="clearCardImage")]
        )
        return card


    def standupCard(self, title, text):
        
        card = HeroCard(
            title=title,
            text=text,
            images=[CardImage(url="https://i.ibb.co/5RvL5gQ/3.png")]
        )
        return card


    def areYouSureCard(self, title, text):
        card = HeroCard(
            title=title,
            text=text,
            buttons=[   
                CardAction(
                    type=ActionTypes.message_back,
                    title="Confirm",
                    text="/clearyesimsure",
                    value="confirm",
                )
            ],
            images=[CardImage(url="https://i.ibb.co/YWzCsNk/4.png")]
        )
        return card

    def tomorrowCard(self, title, text):
        card = HeroCard(
            title=title,
            text=text,
            images=[CardImage(url="https://i.ibb.co/5xq3h3d/6.png")]
        )
        return card

    
    def completeCard(self, title, text):
        card = HeroCard(
            title=title,
            text=text,
            images=[CardImage(url="https://thumbs.gfycat.com/VictoriousBigCopperhead-size_restricted.gif")]
        )
        return card

    

    def toDoCard(self, title, text, prioritySet):
        buttons=[

                CardAction(
                    type=ActionTypes.message_back,
                    title="1",
                    text="/priority 1",
                    value="1",
                ),
                CardAction(
                    type=ActionTypes.message_back,
                    title="2",
                    text="/priority 2",
                    value="2",
                ),
                CardAction(
                    type=ActionTypes.message_back,
                    title="3",
                    text="/priority 3",
                    value="3",
                ),
                CardAction(
                    type=ActionTypes.message_back,
                    title="4",
                    text="/priority 4",
                    value="4",
                )
            ]
        if prioritySet:
            buttons = None
        card = HeroCard(
            title=title,
            text=text,
            buttons=buttons,
            images=[CardImage(url="https://i.ibb.co/hK8wZPN/7.png")],
        )
        return card