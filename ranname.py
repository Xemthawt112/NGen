#Class ranname is an object that contains a string (a name), and all tags
#associatedwith each name. Assumed to be constructed from a csv, expected format
#is [name],tag 1],[tag 2],[tag3],...,[tag n]. Only tags with full implementation
#in current csv are 'masculine','feminine', and 'surname'
class ranname:
    def __init__(self, elements):
        self.name = elements[0]
        elements.remove(self.name)
        taglist=[]
        for i in elements:
            temp=i.replace('\n','')
            taglist.append(temp)
        self.tags = taglist
    #Function that returns all tags in object
    def printtags(self):
        for i in self.tags:
            print i
    #function that returns a bool based on if a tag is in the object
    def checktag(self,check):
        for i in self.tags:
            if i==check:
                flag=True
                break
            else:
                flag=False
        return flag
    #CURRENTLY UNUSED: Functionality for write portion of i/o. Returns object
    #in format printed in a csv. 
    def checkout(self):
        check=[]
        check.append(self.name)
        check.append(self.tags)
        return check
    
        
        
                
