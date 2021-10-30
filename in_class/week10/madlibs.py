import random

random_people = ['Edward', 'Benny', 'Ian']
random_places = ['USF', 'Venezuela', 'the void']
random_adjectives = ['sussy', 'unfortunate', 'crippling']
more_adjectives = ['unlucky', 'tilted', 'broken']
plural_nouns = ['weapons of mass destruction', 'quantum computers stolen from China', 'resold NVIDIA graphics cards']
more_plural_nouns = ['South American coffee beans', 'awful jokes', 'CS homework assignments']
diff_places = ['Bank of China', 'New York Stock Exchange', 'local anime convention']
action_verbs = ['watch the wind go by', 'ask for refunds', 'sit in regret']
more_action_verbs = ['burn', 'eat 5-month old chips', 'lay and ponder their life choices']
foods = ['cold ramen', 'Brussels sprouts', 'meatloaf from yesterday']
nouns = ['Nutella', 'Nickelodeon\'s mystery slime', 'public pool']

print('Last Summer, we went for a vacation with ' + random_people[random.randint(0, 2)] + ' on a trip to ' +
      random_places[random.randint(0, 2)] + '. The weather there is very ' + random_adjectives[random.randint(0, 2)] +
      '! Northern ' + diff_places[random.randint(0, 2)] + ' has many ' + plural_nouns[random.randint(0, 2)] +
      ', and they make ' + more_plural_nouns[random.randint(0, 2)] + ' there.')
print('Many people also go to the ' + diff_places[random.randint(0, 2)] + ' to ' + action_verbs[random.randint(0, 2)] +
      '. The people that live there love to eat ' + foods[random.randint(0, 2)] + '. They also like to ' +
      more_action_verbs[random.randint(0, 2)] + ' in the Sun and swim in the ' + nouns[random.randint(0, 2)] + '.')
print('It was a really ' + more_adjectives[random.randint(0, 2)] + ' trip!')
