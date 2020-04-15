p = open("positive.txt", 'r')
n = open("negative.txt", 'r')

positive = list()
negative = list()

for line in p:
	if line[0].isalpha():
		line = line.strip()
		positive.append(line)

for line in n:
	if line[0].isalpha():
		line = line.strip()
		negative.append(line)

comment1 = "I like your blog You give a very clear description about data analysis on social media The structure is good the examples and description on data retriving analysis and presentation are very detailed Your blog reminded me of my experience of dealing the data myself The dataset has been formed I just needed to reform it so I can apply them on another data analysis tool it still took me several days because of countless small problems The reality is much more complicated the messy information strang characters noise and the flexibility and changable of language cound all be annoy However its also the interesting part and the motivation we analyze ourseleves through social media"
comment2 = "Its a basic and clear description of data analysis on social media However please allow me to point that eve we know what kind of data we need the process of collecting data could still be very hard While some platforms are willing to provide API for sharing data some platforms choose to keep their data privately since data now is becoming an important resource and some platforms only provide limited size of datasets Its still a long way Good luck guys"
comment3 = "I like your blogs style You start from data technology and the importance of social media analysis to explain what is social media analysis which gives us a fresh perspective to look at social media From your blog I focused more on what are social media consist of instead of only focusing on all kinds of definitions And more pictures do make blogs beautiful"
comment4 = "Nice blog You remind me of User Generated Content and user-relationship-centric which are very good perspectives on social media One of the interesting parts in nowadays social media is the individuals are getting more influence on information communication especially when its compared to the traditional methods like television and newspaper Everyone are creating forming and organizing information in their own ways now Besides thanks for recommending many analytic tools in your blog which is very useful I would like to try them"
comment5 = "Im so happy to see someone also mentioned about ancient social media I also shared some content about this in my blog I think current social media are built by both the desire on communication and technologies and the two factors also contribute to each other in history Today we have analysis tools for social media thanks for machine learning algorithms and the development of computers we have technology to support and capture information and we have enough data for analysis Therefore social media analysis becomes possible Since we already know that we can get so much useful information from social media analysis why we dont do it"
comment6 = "Hey Ming Like your article Your article provides us rich resources about education I learned a lot from your article Education is an important method to help people change their lives and rebalance the resources in different areas However education resource itself is also a treaseure resource which is hard to be balanced The situation of limited education resource in some areas is not only caused by the limited realization of local people is also caused by the powerless local government The local government might not have enough resource to support quality education We need to strengthen the global cooperation so we can balance the education resource around the world"
comment7 = "Like your blog But I think the strong institution not only means the local institution but also means the global institution Weve seen many local strong institutions do well in their local area But the contradiction between strong institutions is still a big problem to the whole world A strong global institution can provide a more complete policy for us to solve the world wide problem and enhace the cooperation between countries With more communication between people the misunderstanding between different areas could be elimated The new coronavirus is a good example We should focus on fighting it together instead of blaming each other on spreading the new disease"
comment8 = "Thanks for your introduction about climate change The statistic are very impressive and pursuasive I already start to think about what I have done might produce bad influence to the environment We should make people aware the current situation introduce and encourage more green lifestyle to the public"
comment9 = "So happy to see someone talk about gender equality I agree that the gender inequality is much more serious than before We may not see some obvious gender inequality but the gender inequality does exist everywhere And the word women right are gradually becoming a negative word in Chinese sentiment These all give us warning about gender inequality And this gender inequality not only bothers women but also men If men dont want to be limited in certain impression such as not being allowed to be sad not being allowed to be cared and not allowed to be not working so hard to support a whole family this situation wont be changed unless we achieve gender equality Why we dont look at people without gender It might provide us a more colorful impression on the way we know each other"
comment10 = "Nice blog I am also very concerned about the question of decent work and economic growth as Im a student who tries to find a job too I agree that the education is very important to qualify people to get a job However with the development of our society the speed of elimating and creating jobs are also fast which means there are always a certain number of people losing their jobs because of the change of our society I know this situation is reasonable but the society seems a litte cruel to the people who lose their jobs Therefore I just want to sugget if we can provide some backup for people so everyone can still reeducate themselves even after they enter the society instead of focusing too much on the educates before graduates"
comment11 = "Like your blog Your idea about unitying people to form organization to help people really impresses me Before I read your blog the only method I think about using SMA to protect water is posting more water protection advertisements on social media But you point that we can organize ourseleves through the Internet and find better way to untilize and protect water more efficiently"
comment12 = "Like your blog The part about Trump is quite interesting It reminds of the explanation about global warning by Trevor Noah and Ronny Chieng on Daily Show Their comments about Trump attitude to global warning are quite interesting I greatly recommend it to you It talks about how people try so hard to explain the difference between climate and weather but someone just ignore it because of their interests I think the way we try to protect our environment could be harder and harder in the future But we still can propogate the willing to call for more prople to protect our environment through SMA"
comment13 = "Hi Raby Glad to see your new blog I agree that SMA can help people realize the bias on gender Because social media now gradually bacomes a very important method for us to know the world And in some perspective it is much more richful and realistic than books Through the Internet we can find the gender bias around different areas easier And I think we should not stop at this We can still find gender bias widely exists around the world although it may not be so obvious but the harm is still huge I think we can utilize SMA to expose these gender bias to people and make more people understand how gender bias influences people lives heavily"
comment14 = "I agree that An impressive post or advertising video on social media can challenge many people perception of the stereotype of women and men in the traditional sense of society One of the most meaningful contribution of social media is it gives all of us equal rights on sharing our opinions and experiences Therefore through social media we can expose the gender bias to the society get more attention on the harm of gender bias and make people understand there are still many people suffering from this ridiculous reason"
comment15 = "I agree that we can utilize social media to help people Today social media is not only platforms we sharing opinions it is also an important method for us to see the world Through social media people in poverty can also sell their products learn necessary knowledge through social media Therefore we can first help them to construct basic foundation so they can access social media then we can help them build more connections on social media and guide them to learn knowledge themselves"

respond1 = "Thanks for your comment And thanks for your agreement on studying social media is one of the methods to study ourselves If we look through the analysis we have done on different social media in history it looks like the process we try to know ourseleves Social Media Analysis is a big topic It is not only about technoligies information natural language processing and other modern algorithms it is also about knowing how our society runs Social media is a perspective to look at our society It could be very interesting when we use our own knowledge to figure out us"
respond2 = "Thanks for your comment I agree that all subjects ultimate goal relates to human beings This sentence might not work every times But it will be interesting when we look some subjects in this perspective It will help us think ourselves and the relationship between us and the environment For the last question yes they are for other course"
respond3 = "Thanks for your comment Actually I edited and deleted this blog many times This is a short blog and I did not say too much in it Because my emotion is always changing with the news I received The recent days seemed a little harder to us I didn't find a suitable way to express myself This infectious disease tells me a lot about its differences from other natural disaters The problem is always much more complicated when it envolves more about our human society It is not only a fight to disease it is also a fight to ourselves to learn empathy to understand each other and to learn how to stay in our position and take our own responsibility"
respond4 = "Thanks for your comments The social media actually is the same as our real society except it retians all the records of our behaviors so we can study ourselves according to this So it will be great help for us to study ourselves so we can correct and organize ourselves better"

comments = [comment1, comment2, comment3, comment4, comment5, comment6, comment7, comment8, comment9, comment10, comment11, comment12, comment13, comment14, comment15]
responds = [respond1, respond2, respond3, respond4]



text = open("1155107970.txt", 'r')

sum_positive = 0
sum_negative = 0
total = 0

print("Comments given to my blogs:")
for line in text:
	line = line.strip()
	words = line.split()
	current_sum = 0
	current_negative = 0
	current_positive = 0
	for w in words:
		while(not w[0].isalpha):
			w = w[1:]
		while(not w[-1].isalpha):
			w = w[:-1]

		total += 1
		current_sum += 1
		if w in positive:
			sum_positive += 1
			current_positive += 1
		if w in negative:
			sum_negative += 1
			current_negative += 1

	print("Score:" + str((current_positive - current_negative) / current_sum))

print("")
print("Average Given Comments Score:")
print((sum_positive - sum_negative) / total)

print("")
print("Comments to other classmates:")

sum_positive = 0
sum_negative = 0
total = 0

for comment in comments:
	words = comment.split()
	current_sum = 0
	current_negative = 0
	current_positive = 0
	for w in words:
		while(not w[0].isalpha):
			w = w[1:]
		while(not w[-1].isalpha):
			w = w[:-1]

		total += 1
		current_sum += 1
		if w in positive:
			sum_positive += 1
			current_positive += 1
		if w in negative:
			sum_negative += 1
			current_negative += 1

	print("Score:" + str((current_positive - current_negative) / current_sum))

print("")
print("Average Score of comments to other classmates:")
print((sum_positive - sum_negative) / total)

print("")
print("Responds to other classmates:")

sum_positive = 0
sum_negative = 0
total = 0

for respond in responds:
	words = respond.split()
	current_sum = 0
	current_negative = 0
	current_positive = 0
	for w in words:
		while(not w[0].isalpha):
			w = w[1:]
		while(not w[-1].isalpha):
			w = w[:-1]

		total += 1
		current_sum += 1
		if w in positive:
			sum_positive += 1
			current_positive += 1
		if w in negative:
			sum_negative += 1
			current_negative += 1

	print("Score:" + str((current_positive - current_negative) / current_sum))
	
print("")
print("Average Score of responds to other classmates:")
print((sum_positive - sum_negative) / total)
