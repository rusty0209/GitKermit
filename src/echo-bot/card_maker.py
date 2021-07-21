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


class cardMaker(): 
    def cardmaker(self, title, text):
        card = HeroCard(
            title=title,
            text=text,
            images=[CardImage(url="https://techcrunch.com/wp-content/uploads/2019/09/Keeping-an-Enterprise-Behemoth-on-Course-with-Bill-McDermott-SAPDSC00239.jpg?w=1390&crop=1")])

        return card