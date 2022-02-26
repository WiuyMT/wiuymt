"""
The random module is also imported
"""
import random

"""
As soon as the program runs a message is displayed.
"""

print('Welcome to your tarot card reading. You can choose from a standard \n' +
'reading which displays 3 cards and provides you with a reading of the \n' +
'past, present, or future. You can also decide on a universal reading \n' +
'which displays 6 cards and reveals more in depth details! \n')

"""
Retrieve a list for upright cards and another list for
reverse cards.
"""

list_upright_taro = [['THE FOOL UPRIGHT:', 'A new path in life; beginnings and opportunities beckon. A time \nto feel hopeful, courageous, and young at heart. However, there \nmay be risks ahead, too, so The Fool warns that you look before \nyou leap. By all means embark upon a mad adventure or idealistic \nquest for fulfillment, but take heed of the practicalities. The Fool \nalso heralds fun, entertainment, and falling in love.'], ['THE MAGICIAN UPRIGHT:', "You are poised to make dreams become a reality. This card often \nmarks the time just before an important trip, or the beginning of a \nnew project that is about to flourish, symbolized by the growing \nroses and sun. The conditions for success are just right, so take \naction to empower your business, relationships, or other new venture. \nThis will feel natural, all you'll be in the flow, and full of energy and \nideas. Work will feel like a vocation rather than a chore."], ['HIGH PRIESTESS UPRIGHT:', 'New wisdom; your intuition is expanding as you grow in confidence. \nThe card often arises when you sense you are on the right path, \ncreatively and spiritually. Follow your instincts toward people and \nplaces, and they may take you to the next level of learning. This is an \nemotional card, revealing deep feelings of work you may do in secret.'], ['EMPRESS UPRIGHT:', "Happiness, beauty and nurturing, harmonious home. A good omen for \nrelationships in terms of commitment and stability, The Empress, may \npredict marriage and pregnancy. In a younger person's reading, she can \nreveal the positive influence of a mother or mother-figure, and her \nappearance also shows good health and balanced relationships."], ['EMPEROR UPRIGHT:', 'Protection, advice, and support are forthcoming from a trustworthy man, \nwho may be a father-figure or partner. He indicates that order rules -- he \nmay be authoritarian and perhaps old-fashioned, but he has strength of \npurpose, so he predicts action. Practical problems, such as with building \nwork and money, will be resolved in the long term.'], ['HIEROPHANT UPRIGHT:', "It is time to take sound advice from someone you trust. The Heirophant \noften reveals an authority figure, such as a father, teacher, or other mentor.\nHe symbolizes practical wisdom, so his influence can help you resolve a \nchallenge. This card also denotes a spiritual dimension, so it can indicate \nthat you are about to embark on a new course of learning that will bring \nyou closer to your soul's purpose."], ['THE LOVERS UPRIGHT:', "A successful decision is to be made, which is based upon maturity and \nforesight. Previous tensions or conflicts will be resolved. As the card's \nimage suggests, it's appearance in a reading can show two people \nreuniting after a period of uncertainty. It advises you to follow your heart \nand intuition if you are to take a leap toward achieving a goal. In practical \nterms, The Lovers can also reveal outgrowing an environment, such as a \nyoung person leaving home and taking a step toward independence. "], ['THE CHARIOT UPRIGHT:', 'The drive for adventure. As the charioteer uses the force of his will to bring \ntogether everything he needs for his journey, you move on toward a new \nrelationship or career, although The Chariot can also show an important journey, \nlearning or drive, or a new means of transport. At this time, you show great \ndetermination to get where you want to go -- and you will reach your destination. \nThe horses represent libido, so there is also the frisson of sexual adventure here. \nThe horses, dark and white, echo the dark and light aspects of the journey ahead.'], ['JUSTICE UPRIGHT:', 'The favorable conclusion of a dispute or other ongoing concern, \nproviding that your success is deserved. Legal matters are resolved, \nfrom claims over a property to employment issues. As a general \ninfluence, in a reading, Justice argues for a reasoned, pragmatic \napproach to challenges as opposed to avoidance and denial, or \nextreme responses. Balance is all.'], ['THE HERMIT UPRIGHT:', 'Circumstances dictate that you spend time alone. You seek wisdom, \nbut to find it you need to distance yourself from familiar surroundings \nand perhaps certain friends or family. Time alone will create perspective, \nand encourage healing. The Hermit also shows a recuperation period \nafter an illness or operation.'], ['WHEEL OF FORTUNE UPRIGHT:', 'A twist of fate; circumstances change unexpectedly for the better. It is your turn \nto benefit from spontaneous success and joy, as good things come to you without \neffort. Take up every opportunity and appreciate this halcyon time while it lasts. \nThis shift in your life may also uncover new creative pathways, such as alternative, \nstimulating career, as well as predicting better time financially. Long term plans \ncan now proceed unhindered.'], ['STRENGTH UPRIGHT:', 'Courage, Patients, and persistence are needed to face a potentially dangerous \nopponent. If provoked, be prepared to spend time in negotiation, and stand your \nground. Aims can be achieved with quiet confidence rather then displays of overt \nstrength. This card is also about internal conflict and the necessity of accepting \nyour shadow side. In a generally positive reading, Strength also symbolizes \ngood health.'], ['HANGED MAN UPRIGHT:', 'Time out; an opportunity to step back from a situation, such as giving up a belief, \nor perhaps letting go of a dream. As this card literally shows, you may need to hang \naround waiting for someone else to make a decision. In this case, there is little you \ncan do but wait. Analyze the situation with detachment and you may see new \nopportunities from a distance, rather than obsess about an outcome you are \npowerless to change.'], ['DEATH UPRIGHT:', 'The end of a life-phase; relationships, a career, or even an era comes to a close. \nAccept that this is necessary change -- from a friend you have grown away from, \nto a commitment that has restricted your creativity. When you break outdated ties, \nnew people and prospects are free to enter your world. Change is coming, and it is \nbetter to embrace it than to resist; it may be a blessing in disguise.'], ['TEMPERANCE UPRIGHT:', 'Moderation, balance, and patience are essential for the control of volatile influences \nand opposing demands. There is potential for progress as a business, relationship, \nor family grows; use your experience and diplomacy to harmonize conflict and keep \nprojects moving forward. This card also suggests reconciliation, so relationships \ncan be repaired.'], ['THE DEVIL UPRIGHT:', 'Temptation or enslavement to and ideal. Misdirected passion is \nindicated here, such as a dead-end affair, or becoming trapped \nby ambition, perhaps investing energy or money in the wrong \nperson or project for short-term gain. There is a danger that you \nurge for power, to rule. The spell can be broken if you are willing \nto make a small sacrifice now to gain something more rewarding \nin the future.'], ['THE TOWER UPRIGHT:', 'Shock, loss, and insecurity; the collapse of an ideal or relationship.\nThe tower is an construction of hope and ambition, which is destroyed \nby the primal energy of fire. This disaster also symbolizes the tower \nof the ego or pride before a fall. What you have fabricated falls \ndown, and there is little you can do to avoid the situation or repair \nit. Yet you can begin again, and be all that stronger for it.'], ['THE STAR UPRIGHT:', "Inspiration and guidance; you have clarity or purpose and great \npotential now. The water symbolizes creativity and it's flow, memory. \nAs the past and the present flow together, so past experiences give \nyou the wisdom to make a dream come true. This is a nurturing card, \nshowing that you are tending your garden well. Ideas flourish as you \ncreate fertile conditions for success and happiness."], ['THE MOON UPRIGHT:', 'A dilemma; grave or suppressed doubts about how to move forward \nin a relationship, project, or other negotiation close to the heart. This \nis a solitary card, so you may need to come to a decision on your own. \nIf you feel trapped, look beyond what you think is possible, the dog and\nthe wolf silhouetted in The Moon are guardians of boundaries, showing \nlimitations may be self-imposed. As the emotional moon symbolizes \nintuition, your dreams may hold guiding messages.'], ['THE SUN UPRIGHT:', 'Success; time for the good times in life: love, sunshine, rest and play. \nThis may be an extended trip, or time to travel farther afield, but the \nmessage is recuperation rather than adventure. The Sun also describes \nthe honeymoon period of a new relationship; in love, you feel like a child \nagain, innocent and carefree. The card can also signify children coming \ninto your life. The hills shelter the sunflowers from harsh water until they \nare taller, just as a relationship, project, or family is nurtured.'], ['JUDGEMENT UPRIGHT:', 'Judgement predicts a significant life change as a project or relationship \nreaches a conclusion. Before you can leave the past behind, you may need \nto examine your conscience and review your previous actions. Judgement \noffers second chances and an opportunity for forgiveness, along with \nfinancial reward for past efforts that will help your future success. Events \nare about to speed up.'], ['THE WORLD UPRIGHT:', 'Success and happiness; a dream come true. Whatever your goal you will \nachieve it and feel satisfied and rewarded. This is a time of celebration and \njoy, when a project is concluded or you commemorate happy occasions, such \nas wedding anniversaries or birthdays. Whatever difficulties you have faced in \nthe past, your current triumph is applauded by all. Travel may become \npossible now.']]

list_reverse_taro = [['THE FOOL REVERSED:', 'An error of judgement. Bad advice takes you in the wrong direction, \nso investigate all offers carefully. The Fool reversed can also show \ndeception. You may also be trying to force a situation, which can \nonly backfire.'], ['THE MAGICIAN REVERSED:', "Trickery; great plans have no foundation. This card often warns of \nothers' motives, and they may not have your best interest at heart. \nIt may also reveal frustration as, although you feel ready to move on, \nyou meet restriction at every turn. If you are involved in the arts, \na creative block is indicated."], ['HIGH PRIESTESS REVERSED:', 'Hidden information that may cause shock or disappointment is about \nto come to light. A secret is revealed that may incriminate someone you \nthought was above reproach. A trusted mentor is not all he or she seems. \nTake care whom you consult and confide in just now, from physics to older \nfemale relatives.'], ['EMPRESS REVERSED:', 'The reversed Empress reveals difficulties with an older woman, such as a \nparent or mother-in-law, possibly involving clinginess or jealousy. Money \nproblems at home manifest as miserliness or dangerous overspending. This \ncard can also reveal parenting issues, which may involve confrontation.'], ['EMPEROR REVERSED:', "The Emperor reversed is a possessive, stubborn individual who wants to \ncontrol others. You may be the victim, but examine your behavior because \nyou may be dominating a person or situation needlessly. Whatever the \nsituation, you or someone you know is losing perspective: it's time to \ntake a step back. "], ['HIEROPHANT REVERSED:', 'The influence of an oppressive, older person who harangues you with \nunmasked-for advice. Do not be deceived by someone older in years \nbecause you assume they are wiser. The information may be wrong, \nand they may use their status to manipulate you.'], ['THE LOVERS REVERSED:', 'Break-ups and commitment issues: one person may pull away from a \nrelationship rather than work through difficulties. Tension mounts as \nimbalance and temptation creep in, such as seeking out an affair as a \nway of avoiding problems. Otherwise, this immaturity may be expressed \nas over dependence on a parent.'], ['THE CHARIOT REVERSED:', 'Ego and arrogance bring problems. Progress comes to a halt, or you feel that you \nare going in the wrong direction. On a mundane level, there could be a problem \nwith transport, as plans go awry and a journey is delayed or abandoned.'], ['JUSTICE REVERSED:', 'In the reversed position, Justice shows a miscarriage or justice. \nA decision goes against you, or a straightforward situation becomes\nunnecessarily complicated and the true facts of the matter become \nhidden. Others may act with bias, and you may overlook those who \ncan support you at this difficult time. Judge yourself kindly and hold \nfast to your beliefs.'], ['THE HERMIT REVERSED:', 'Enforced isolation. Refusal to learn or listen to advice may result in withdrawal\nfrom others in anger or resentment. You may need more time to come to terms\nwith a situation you do not wish to accept. The Hermit reversed can also show\nan over analysis and a tendency to intellectualize rather than allowing feelings \nto surface.'], ['WHEEL OF FORTUNE REVERSED:', 'The reversed wheel shows a downturn in fortune. You may have little influence \nover events at this time, but the situation will not prevail. As the wheel goes against \nyou, so it can turn again in your favor.'], ['STRENGTH REVERSED:', 'Curb baser instincts, such as overindulgence in food or overspending. Difficult \nemotions, such as anger, may need to be dealt with. You may be inclined to run \naway from problems rather than risk confrontation.'], ['HANGED MAN REVERSED:', 'Betrayal, often of the self. You may shy away from making a life-changing decision \nbecause it means initial discomfort or expense, and even yearn to return to the life \nyou has as a dependent child. It is time to wake up from the reverie and confront \nwhatever is causing anxiety.'], ['DEATH REVERSED:', 'An inability to give up what has already been taken. You may be living in the past \nmore then you realize. Until you let go of the people or possessions that no longer \nrepresent who you are, or want to be, new opportunities are blocked. Surrender \nrather than waste time and energy clinging to suffocating familiarity. '], ['TEMPERANCE REVERSED:', "You may feel overwhelmed, bonded to others' demands and under increasing \npressure to cope. Money problems are often involved, so it is vital you deal with \npotential debt or resolve a deficit of time and energy."], ['THE DEVIL REVERSED:', 'Obsession, such as an unhappy, destructive affair. When reversed, \nThe Devil shows and inability or unwillingness to break a bond that \nhas no future, due to immaturity, desperation, or low self-esteem. \nThe card may indicate a struggle with addiction.'], ['THE TOWER REVERSED:', 'An avoidable disaster. Your worst fears are realized as a relationship, \nbusiness venture, or home project collapses -- and you know that you \nmay be partly to blame. However, after anger at the sense of injustice \ncomes guilt and, finally, a sense of relief. A struggle ends.'], ['THE STAR REVERSED:', "A creative or an emotional block, arises as a project or partnership \nloses it's way. You need direction, but beware of those who cultivate \nyou for their own purpose. You may need to step out of an illusion \nand search for your star elsewhere."], ['THE MOON REVERSED:', "A failure of nerve. You do not trust your feelings and look to others for \nanswers. Over dependence on a mentor figure could show you have \nbegun to doubt your instincts. Moonlight can be deceptive -- so \nexamine others' motives carefully before you commit. Don't settle \nfor second best. "], ['THE SUN REVERSED:', 'Delay & Frustration. Your goal is just out of reach. Work or illness obstruct \nplans, and the paradise you had, envisaged is perilously close to slipping \naway. Vacations are cancelled, or a relationship does not materialize. \nPhysically, your energy levels may be depleted.'], ['JUDGEMENT REVERSED:', 'Daily, due to the past getting in the way, or fear of change. You may judge \nyourself too harshly, or allow others to disregard your contribution, although \nthis may be an excuse for not being able to let go. You may need to \nre-examine your attitudes and overcome feelings of guilt. What counts is \nwhat you believe about yourself.'], ['THE WORLD REVERSED:', 'Restriction. Failure to move forward is often due to indecision or negativity. \nThrough feelings of being trapped in the past, or by the needs of others, \nyour world seems to be growing smaller rather than expanding to welcome \nnew people and opportunities. If you address what is really holding you back \nthere is a chance for you to achieve your dream.']]

while True:
    """
    while True keeps the user input alive
    """
    try:
        """
        try block is added for exception handling
        """

        # prompt user to enter an option
        user_input = int(input(
            "\nWhat type of tarot reading would you like? Please\n"
            "enter a number that corresponds to an available option.\n"
            "1: Standard Major Arcana Spread\n"
            "2: Universal Major Arcana Spread\n"
            "3. Exit\n"
            "Enter a choice: "))

        if user_input == 1:
            """
            If user input is equal to 1 then display a 3 card
            tarot spread
            """

            # randomize list to show
            # 2 random upright cards and
            # 1 random reverse cards
            list_reverse_random = random.sample(list_reverse_taro, 2)
            list_upright_random = random.sample(list_upright_taro, 1)

            # combine reverse card list and upright card list
            list_taro_deck = list_reverse_random
            list_taro_deck.extend(list_upright_random)

            # randomize combined list
            list_taro_deck = random.sample(list_taro_deck, 3)

            # create headers for each card displayed
            # make it a set to remove duplicates
            set_taro_header_standard = {'~~ Draw 2 : The Present ~~',
                                        '~~ Draw 1 : The Past ~~',
                                        '~~ Draw 1 : The Past ~~',
                                        '~~ Draw 3 : The Future ~~'
                                        }
            # turn set header to a tuple and sort
            set_taro_header_standard = sorted(tuple(set_taro_header_standard))

            # turn final card deck to dictionary and back to list
            dic_taro_deck = {k: v for k, v in list_taro_deck}
            list_taro_deck = list(dic_taro_deck.items())

            # create header to display with tarot card reading
            print("\n\n\n||==========" +
                  "~~~~~ STANDARD TAROT READING ~~~~~"
                  + "=========||\n")

            # print out reading header, draw number, card and description
            for x, (k, v) in zip(set_taro_header_standard, list_taro_deck):
                print("||==========" + x + "=========||")
                print("||==========" + k + "=========||")
                print(v, "\n")

        elif user_input == 2:
            """
            If user input is equal to 2 then display a 6 card
            tarot spread
            """

            # randomize list to show
            # 4 random upright cards and
            # 2 random reverse cards
            list_reverse_random = random.sample(list_reverse_taro, 4)
            list_upright_random = random.sample(list_upright_taro, 2)

            # create final list and randomize it
            list_taro_deck = list_reverse_random
            list_taro_deck.extend(list_upright_random)
            list_taro_deck = random.sample(list_taro_deck, 6)

            # create tuple for headers for each card displayed
            tuple_taro_header_universal = (
                '~~ Draw 1 : How you feel about yourself ~~',
                '~~ Draw 2 : What you want most right now ~~',
                '~~ Draw 3 : Your fears ~~',
                '~~ Draw 4 : What is going for you ~~',
                '~~ Draw 5 : What is going against you ~~',
                '~~ Draw 6 : The likely outcome ~~',
                                           )

            # turn final deck to dictionary and back to list
            dic_taro_deck = {k: v for k, v in list_taro_deck}
            list_taro_deck = list(dic_taro_deck.items())

            # create header to display with tarot card reading
            print("\n\n\n||==========" +
                  "~~~~~ UNIVERSAL TAROT READING ~~~~~" +
                  "=========||\n")

            # print out reading header, draw number, card and description
            for x, (k, v) in zip(tuple_taro_header_universal, list_taro_deck):
                print("||==========" + x + "=========||")
                print("||==========" + k + "=========||")
                print(v, "\n")

        elif user_input == 3:
            """
            If user selects 3, display bye
            message and exit the program
            """
            print("BYE! Come back again soon!")
            break

        else:
            # If user enter an integer thats not 1, 2, or 3
            # The following message is displayed
            print(user_input, "is not a valid option, please try again.\n\n")

    except ValueError:
        """
        value error exception displays a message for all other
        non integer inputs entered.
        """
        # catches all other inputs enter str, float, etc
        print("ERROR: Please enter a valid option. "
              "Valid options are integers 1, 2, or 3\n\n")
