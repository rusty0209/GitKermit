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
        if type == "todopriorityset":
            return self.toDoCard(title,text, True)
        elif type == "show":
            return self.showCard(title,text)
        elif type == "complete":
            return self.completeCard(title,text)
        elif type == "remove":
            return self.removeCard(title, text)
        elif type == "edit":
            return self.editCard(title, text)
        elif type == "clear":
            return self.clearCard(title, text)
        elif type == "tomorrow":
            return self.tomorrowCard(title, text)
        elif type == "are you sure":
            return self.areYouSureCard(title, text)
        elif type == "status":
            return self.statusCard(title, text)
        elif type == "priority":
            return self.priorityCard(title, text)
        elif type == "description":
            return self.descriptionCard(title, text)
        elif type == "standup":
            return self.standupCard(title, text)
        elif type == "help":
            return self.helpCard(title, text)
        elif type == "spelling":
            return self.spellingCard(title, text)
    
    def helpCard(self, title, text):
        card = HeroCard(
            title=title,
            text=text,
            #images=[CardImage(url="clearCardImage")]
        )
        return card
    
    def spellingCard(self, title, text):
        card = HeroCard(
            title=title,
            text=text,
            images=[CardImage(url="https://i.kym-cdn.com/photos/images/newsfeed/001/762/118/72c.jpg")]
        )
        return card
    
    def priorityCard(self, title, text):
        card = HeroCard(
            title=title,
            text=text,
            #images=[CardImage(url="clearCardImage")]
        )
        return card

    def descriptionCard(self, title, text):
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
            #images=[CardImage(url="clearCardImage")]
        )
        return card

    def statusCard(self, title, text):
        card = HeroCard(
            title=title,
            text=text,
            #images=[CardImage(url="clearCardImage")]
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
            #images=[CardImage(url="clearCardImage")]
        )
        return card

    def tomorrowCard(self, title, text):
        card = HeroCard(
            title=title,
            text=text,
            #images=[CardImage(url="clearCardImage")]
        )
        return card
    
    def clearCard(self, title, text):
        card = HeroCard(
            title=title,
            text=text,
            #images=[CardImage(url="clearCardImage")]
            
        )
        return card
    
    def editCard(self, title, text):
        card = HeroCard(
            title=title,
            text=text,
            #images=[CardImage(url="clearCardImage")]
        )
        return card
    
    def completeCard(self, title, text):
        card = HeroCard(
            title=title,
            text=text,
            #images=[CardImage(url="clearCardImage")]
        )
        return card
    
    def removeCard(self, title, text):
        card = HeroCard(
            title=title,
            text=text,
            #images=[CardImage(url="clearCardImage")]
        )
        return card
    
    def showCard(self, title, text):
        card = HeroCard(
            title=title,
            text=text,
            #images=[CardImage(url="clearCardImage")]
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
            images=[CardImage(url="https://techcrunch.com/wp-content/uploads/2019/09/Keeping-an-Enterprise-Behemoth-on-Course-with-Bill-McDermott-SAPDSC00239.jpg?w=1390&crop=1")],
        )
        return card