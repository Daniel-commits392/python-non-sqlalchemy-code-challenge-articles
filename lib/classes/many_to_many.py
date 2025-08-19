class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        author.articles.append(self)
        magazine.articles.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        if not isinstance(value,str):
            raise ValueError('Title must be a string')
        if len(value)<5 or len(value)>50:
            raise ValueError('Title has to be between 5 and 50 characters')
        if hasattr(self,'_title'):
            raise AttributeError('Title cannot be changed once set')
        self._title=value
    

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,value):
        if  not isinstance(value,Author):
            raise ValueError('Must be of type Author')
        self._author=value
    

    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,value):
        if not isinstance(value,Magazine):
            raise ValueError('Must be of type Magazine')  
        self._magazine=value 


class Author:
    def __init__(self,name):
        self.name=name
        self.articles=[]

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if  not isinstance(value,str):  
            raise ValueError('The name must be a string')
        if len(value)==0:
            raise ValueError('Name must be longer than 0 characters')
        if hasattr(self,'_name'):
            raise AttributeError('Name cannot be changed once set')
        self._name=value
   
    def magazines(self):
       pass

    def add_article(self, magazine, title):
       return Article(self, magazine, title)
    def topic_areas(self):
        pass


class Magazine:
    def __init__(self,name,category):
        self.name=name
        self.category=category
        self.articles=[]

    @property
    def name(self):
        return self._name 
    @property
    def category(self):
        return self._category  
    
    @name.setter
    def name(self,value):
        if  not isinstance(value,str):
            raise ValueError('Name must be a string')
        if len(value)<2 or len(value)>16:
            raise ValueError('Name must be between 2 and 16 characters')
       
        self._name=value

    @category.setter 
    def category(self,value):
        if not isinstance(value,str):
            raise ValueError('Category must be a string') 
        if len(value)==0:
            raise ValueError('Category must be greator than 0')  
        
        self._category=value


   
    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass


author = Author("Carry Bradshaw")
magazine = Magazine("Vogue", "Fashion")
article_1 = Article(author, magazine, "How to wear a tutu with style")



    
   
   
   
   
   
   
   
   
   
   
   
   
   
    # my pseudocode 

# class Author:
#     def __init__(self,name):
#         self.name=name
#         self.articles=[]

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self,value):
#         if  not isinstance(value,str):  
#             raise ValueError('The name must be a string')
#         if len(value)==0:
#             raise ValueError('Name must be longer than 0 characters')
#         if hasattr(self,'_name'):
#             raise AttributeError('Name cannot be changed once set')
#         self._name=value

# # to create relationships create a list for articles in the magazine and author classes
# #then append the list to the article class


# class Magazine:
#     def __init__(self,name,category):
#         self.name=name
#         self.category=category
#         self.articles=[]

#     @property
#     def name(self):
#         return self._name 
#     @property
#     def category(self):
#         return self._category  
    
#     @name.setter
#     def name(self,value):
#         if  not isinstance(value,str):
#             raise ValueError('Name must be a string')
#         if len(value)<2 or len(value)>16:
#             raise ValueError('Name must be between 2 and 16 characters')
       
#         self._name=value

#     @category.setter 
#     def category(self,value):
#         if not isinstance(value,str):
#             raise ValueError('Category must be a string') 
#         if len(value)==0:
#             raise ValueError('Category must be greator than 0')  
        
#         self._category=value
