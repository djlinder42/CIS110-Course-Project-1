print(f"Hello, Would you like to hear a story about a farmdog?")
print(f"Before we get started, I have a few questions for you.")
print(f"After typing your answer, please press the enter key.")
input(f"/nPress the enter  key to continue...")
breed = input(f"\nWhat breed is your favorite dog:  ")
while len(breed) == 0:
    breed = input(f"Please enter a breed:  ")
dogName = input(f"What is your favorite dog's name:  ")
while len(dogName) == 0:
    dogName = input (f"Please enter a dog's name:  ")
city = input(f"What major city do you live nearby:  ")
while len(city) == 0:
    city = input(f"What city do you live near?:  ")
pond = input(f"What is your favorite swimming hole:  ")
while len(pond) == 0:
    pond = input(f"Please type the name of your favorite swimming hole:  ")
number = input("What is your favorite number?  ")
while not number.isdigit():
    number = imput(f"Value is not recognizd. Please enter a numeric value:  ")
    
print(f"\nLET'S GO!!!!!")
print(f"\nOnce upon a time there was a {breed} farmdog that was named {dogName}.  ")
print(f"{dogName} was rounding up the sheep before he leaves for {city}.  ")
print(f"{dogName} loves to swim, and he feels like today he may have have the chance.  ")
print(f"{dogName} turns toward the pond and runs as fast and as hard as he can.  ")
print(f"While running as fast as he can, {dogName} finally arrives at {pond}. Before jumping in though, he begin's to think.  ")
jumpIntoPond = input(f"\nShould {dogName} jump into {pond}? Type yes or no:  ")
while jumpIntoPond.lower() != "yes" and jumpIntoPond.lower() != "no":
    jumpIntoPond = input("Please type yes or no:  ")
if jumpIntoPond == "yes":
    print(f"\n{dogName} jumps into {pond} splashing and having a great time!  ")
    print(f"When the coyotes notice {dogName} playing and paying no attention to his flock of sheep.  ")
    print(f"They creep in slowly as to not arouse suspicion.  ")
    print(f"Oblivious to the approaching danger, {dogName} gets out of the water accidently falling asleep.  ")
    print(f"{dogName} falls into a deep sleep as the coyote gets closer andd closer.  ")
    print(f"Luckily {dogName} opens his eyes with no time to spare, narrowly escaping unharmed.  ")
else:
    print(f"\n{dogName} decides that it's just to risky to play in the water with hidden danger around every corner.  ")
    print(f"Being a responsible {breed}. {dogName} decides to do a quick scan of the area, when he spots movement in the bushes.  ")
    print(f"Knowing he has {number} sheep to protect. {dogName} slowly begins moving toward the bushes.  ")
    print(f"A mouse!! {dogName} felt relieved to see a little harmless mouse just searching for food.  ")
attackTheCoyote = input(f"\nShould {dogName} attack the coyote approaching his flock? Type yes or no:  ")
while attackTheCoyote.lower() != "yes" and attackTheCoyote.lower() != "no":
    attackTheCoyote = input(f"Please type yes or no:  ")
if attackTheCoyote == "yes":
    print(f"\n{dogName} locks onto the coyote with his eyes, knowing his only job is to protect the {number} sheep in his flock.  ")
    print(f"{dogName} uses the tall grass for coverage as he sneaks closer and closer.  ")
    print(f"{dogName} isn't scared at all, all of his sences hightened.  ")
    print(f"{dogName} pounces on his target, swiftly and powerfully neutralizing the danger.  ")
else:
    print(f"\n{dogName} decided to keep his distance, exactly {number} inches away.  ")
    print(f"Being a cautious {breed} dog, {dogName} uses the tall grass for camoflauge.  ")
    print(f"{dogName} doesnt attack, but he does makes sure the coyotes keeps a safe distance away from his flock.  ")
    keepPlaying = input(f"\nWould you like to play again? Enter yes or no:  ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"Please type yes or no:  ")
if jumpIntoPond == "yes" and attackTheCoyote == "yes":
    print(f"After spending the day protecting his flock {dogName} sneaks into the {pond} watering hole.  ")
    print(f"{dogName} is bitten by a snapping turtle.  ")
    print(f"Luckily {dogName} yelled for all {number} of his sheep to stampeed the water.  ")
    print(f"All {number} sheep come to the rescue of {dogName}.  ")
elif jumpIntoPond == "no" and attackTheCoyote == "no":
    print(f"After spending all day protecting his flock {dogName} has also gotten to play in {pond}.  ")
    print(f"Luckily {number} of sheep in his flock was able to scare the turtle off of his tail.   ")
    print(f"{dogName} decides he has had enough for one day and decides to turn in before glancing at {pond} once more before bed.  ")
    print(f"{dogname} cant believe the day he's had. From the coyotes to the snapping turtles in the {pond}  ")
else:
    print(f"\nAfter spending the day protecting his flock {dogName} sees something shiny, and wonders if it's from {city}.  ")
    print(f"{dogName} farmer friend has gotten him a brand new collar with gps.  ")
    print(f"{dogName} loves to play in {pond} but he also knows the dangers that lurk around every corner.  ")
    print(f"{number} of sheep depend on the vidualance of {dogName} to survive.  ")
print("\nThe End")
         