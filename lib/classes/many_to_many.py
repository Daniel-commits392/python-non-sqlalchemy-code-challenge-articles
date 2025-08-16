class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    all=[]
    def __init__(self, name):
      if not isinstance(name,(str)):
          raise ValueError('The name must be a string')
      if len(name)==0:
          raise ValueError('The name cant be less than 0 characters')
      self.name=name
      
    @property
    def name(self):
        return self.name 
    @name.setter
    def name(self):
        if hasattr(self,'name'):
            raise AttributeError('Cannot change authors name once set')
    
   
    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass