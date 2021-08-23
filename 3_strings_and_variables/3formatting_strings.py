#Formatting String
 print('I {} Python.'.format('love'))
 print ('{} {} {} '.format('I', 'love', 'Python'))

 print('I {0} {1}. {1}{0}s me.'.format('love', 'Python'))

 #Formating Strings
 print(' {0:8} | {1:8}'.format('Fruit', 'Quantity') )
 print(' {0:8} | {1:8}'.format('Apple', 3) )
 print(' {0:8} | {1:8}'.format('Oranges', 10) )

 #Formating Strings Alignment
 # < Left
 # ^ Center
 # > Right

 #Formanting Strings - Data Types

 #f Float
 #.Nf N = The number of decimal places

 #Example{:.2f}

 print(' {0:8} | {1:8}'.format('Fruit', 'Quantity') )
 print(' {0:8} | {1:8.2f}'.format('Apple', 2.3333) )
 print(' {0:8} | {1:8.2f}'.format('Oranges', 10) )



 #Getting User Input
 fruit = input('Enter a name of a fruit: ')
 print ('{} is a lovely fruit.'.format(fruit))