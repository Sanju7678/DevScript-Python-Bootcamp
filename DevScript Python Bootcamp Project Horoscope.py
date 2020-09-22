#Python Bootcamp Project: Applications that tells Horoscope by using Zodiac Sign

print("Today's Horoscope")
next = True
while next == True:
	print('''
1. Aries
2. Taurus
3. Gemini
4. Cancer
5. Leo
6. Virgo
7. Libra
8. Scorpio
9. Sagittarius
10. Capricorn
11. Aquarius
12. Pisces	
	''')
	s=int(input('Pick your sign number and press Enter: '))
	if s==1:
		print("Your Chosen Zodiac Sign is 'Areies'. Today's Horoscope:")
		print("Today, the stars put you on high alert... and not for nothing. You will save yourself from being swindled. Though you will easily manage to stay ahead of others, you may make a few enemies on your way. It's not a good day if you're looking to buy a house or vehicle, says Ganesha.")
	
	elif s==2:
		print("Your Chosen Zodiac Sign is 'Taurus'. Today's Horoscope:")
		print("Your enthusiasm will be as contagious as your smile today, predicts Ganesha. People will stand charmed by your high spirits. There will be stressful moments, but things will look up later in the day. Take some time off if things get too hectic for you.")
	
	elif s==3:
		print("Your Chosen Zodiac Sign is 'Gemini'. Today's Horoscope:")
		print("Bosses will assign new responsibilities to you, predicts Ganesha. Your daytime distress, however, will transform into jubilation by the end of the day's work, as you will be able to produce brilliant results. Ganesha advises you to delay bidding for tenders by a few days.")
	
	elif s==4:
		print("Your Chosen Zodiac Sign is 'Cancer'. Today's Horoscope:")
		print("You may be in one of your more frivolous moods today, foresees Ganesha. Gossip, fun, laughter and some harmless flirting shall make your day interesting, yet these are not the pastimes you usually enjoy. Hence, as the day rolls on, you shall find yourself to your reserved, reticent self concentrating hard on getting the work done to make way for the early evening gym/ driving class. Good going, after all finding balance is just the right thing to do.")
	
	elif s==5:
		print("Your Chosen Zodiac Sign is 'Leo'. Today's Horoscope:")
		print("Talk of being busy! It seems like today, you shall take the cake, and perhaps, be the icing on it as well, says Ganesha. It is likely that the day is going to be very hectic for you in terms of work and business. You may be engaged in official conversations and dealings. Also, don't be surprised to find yourself in meetings as you attempt to take stock of your business situation. After such a long and tiring day, it is only normal for you to unwind later in the evening with your sweetheart, feels Ganesha.")
	
	elif s==6:
		print("Your Chosen Zodiac Sign is 'Virgo'. Today's Horoscope:")
		print("The booster rockets of your ambitions and spirit to work will kick in at the maximum today. Seek recreation after a hard day's work and look to relax at private parties, social-dos and even weddings, says Ganesha.")
	
	elif s==7:
		print("Your Chosen Zodiac Sign is 'Libra'. Today's Horoscope:")
		print("You may not have been crowned ‘Employee Of The Month', but do not let that distract you from the fact that today, you are the brightest star in office. Be prepared to get some special treatment at work, as your bosses shower praise on you. Apart from that, a lot of tangible and intangible benefits await you. Ganesha advises you against complacency of any sort if you want the key to the executive wash room.")
	
	elif s==8:
		print("Your Chosen Zodiac Sign is 'Scorpio'. Today's Horoscope:")
		print("You shall probably realise the fact that seeing is believing. Learn to trust your own eyes more than what you hear. Don't get lost in the crowd, warns Ganesha. Strive to stand out and be in the spotlight, advises Ganesha.")
	
	elif s==9:
		print("Your Chosen Zodiac Sign is 'Sagittarius'. Today's Horoscope:")
		print("Round and round they tumble, the wheels of life, smoothly gliding into a routine. You may spend your day in discontent due to the rut of regular activities. Sadly, there is little hope or adventure Ganesha foresees that might make this day worthwhile for you. There will be glimpses of excitement in the evening but on the whole, it will be nothing to write home about.")
	
	elif s==10:
		print("Your Chosen Zodiac Sign is 'Capricorn'. Today's Horoscope:")
		print("Duping the wisest with your extraordinary power of convincing may have been your forte, but you may have to prove yourself all over again, for Ganesha says you will be tested today. This apart, you are likely to find answers to questions lingering in your subconscious mind for long. The outburst of creativity in the second half of the day will draw the attention of your peers, and this will also be the best time to seek their support, advises Ganesha.")
	
	elif s==11:
		print("Your Chosen Zodiac Sign is 'Aquarius'. Today's Horoscope:")
		print("For a moment, it seems that you're swamped with problems. But you are brave enough to deal with any ugly issue that crops up suddenly. Ganesha hints at a romantic evening, which may just be time together in a jacuzzi, or simply preparing a meal together. Pure ecstasy!")
	
	elif s==12:
		print("Your Chosen Zodiac Sign is 'Pisces'. Today's Horoscope:")
		print("All the dieting that you have been undergoing will finally begin to show results, with compliments galore coming your way from your friends. Your energy and enthusiasm levels are likely to be high. A bright and beautiful day waits, says Ganesha.")
	
	else:
		print("Hey, You sure about the number?")
	
	print('')	
	temp=input("Shall we do it again? (Y/N):")
	if temp=='Y':
		next=True
	else:
		next=False