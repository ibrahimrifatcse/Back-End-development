# python data type
1. Numeric         
* int 
* float 
* complex number 

2. sequence    
* string 
* list 
* tuples

3. Dictionary  
4. Boolean    
5. set
       

### Numeric
                                                
>          int = 12
>          float = 12.6
>          complex number = 12 + 12i

###  sequence

##### string : A string is a sequence of characters that is enclosed is either a single or double quotes.
>           name = " ibrahim rifat"
 
####  List : list are a sequence of one or more different or similar type . They are essentially an array and hold any type inside square brackets. Each item can be accessed by its index.
>           list = [1,'hello',4.5,"A"]
  
#### Tupple : Tupple are similar to lists in many ways.  They contain an ordered sequence of one of more types, but main defference is that they are immutable. They cannot be modified or changed.
            
>     exampleTupple = (1,'hello', 4.5,"A")
>        print(exampleTupple[1])
  
### Dictionary
####  Dictionary store data in a key value object structure. Each vlaue can be accessed by directly by it's key.
####  Dictionary can also store any data type.
>           ed = {'a':22, 'b':44.4}
>           ed[a]
>    #output: 22
   
###  Boolean
>     true || false
   
                                              
###  Data type

####  string

>               name= 'ibrahim'
>               print(len(name)
>               #output
>               =  7
>                a='hello'
>               b="hello"
>               #backslash has the effect of joining
>                b ='sorry I wish to interrupt you there' \
>                   ' In addition that'
>                    
>               a= 'you are right however'
>               b=' I don't fully endorse your statement'
>              
>               print(a+b)   #concatenation
>               =>  you are right however I don't fully endorse your statement
>                
>               # take input from user
>               a= 'you are right however'
>               b= input('enter your line : ') # or b= input()
>               print(a+b)
                
##     convert

        # this function can be used to convert the provide vlaue 
>         int('75')
>         75
>         str(55)
>         '55'
>         int_x = 10
>         float(int_x)
>    #output :     10.0
                
##         function create

>                 def greating(person)
>                    print("welcom" + person)
>                    
>               greating(ibrahim)
>               #output :  welcome ibrahim
                
## Type casting

                                         
>           int(), float(),str()
>           1. ord() = which returns an integer representing the underlying unicode character
>           2. hex() = int to hexadecimal string
>           3. oct() = returns a string representing an oct to number.
>           4. tuple()  
>           5. set() 
>           6. list()
>           7. dict()
           
###           sep funtion

>                    print('ibrahim','rifat') => ibrahimrifat
>                    print('ibrahim','rifat',sep=', ') => ibrahim rifat
                      
                      
###      direct formating
                                      
>                a=12
>                b=5
>                ans=a+b
>                print('Addition the value of {} and {}= {}'.format(a, b, ans))
                                      
###     output formating

>                        print('I like  {0} more than {1} '.format("oranges", "grapes"))
>                        print('I like  {1} more than {0} '.format("oranges", "grapes"))                      
                                              
###     type 

>                      num1=input('enter first number : ')
>                      num2=input('enter second number : ')
>                      print(type(num1))
>                      print(type(num2))
>                      print(num1 + num2 )
>
>                   nums1=input('enter first number : ')
>                   nums2=input('enter second number : ')
>
>          print(int(nums1) + int(nums2) )

                                              
###             type 

>                   str1=input('enter your first name : ')
>                    str2=input('enter your second name : ')
>
>                    print('hello {} {}'.format(str1, str2))
>                    #output : hellow ibrahim rifat                          
                                              
