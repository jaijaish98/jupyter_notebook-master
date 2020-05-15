# import logging
# import webbrowser
#
#
# class AmazonSDEJobApplication:
#     logging.info("Job application for the position of Software Development Engineer @ Amazon")
#
#     def __init__(self, name, location, email, contact_number):
#         self.personalInfo = dict()
#         self.personalInfo["Name: "] = name
#         self.personalInfo["CurrentLocation: "] = location
#         self.personalInfo["Email: "] = email
#         self.personalInfo["ContactNumber: "] = contact_number
#
#     def build_resume(self):
#         print("Creating my profile for your reference")
#         experience = self.get_experience()
#         edu_details = self.get_educational_details()
#         social_media_contact = self.get_social_media_contacts()
#         resume = open("JAYENDRAN_RESUME.txt", "w")
#         resume.write(str(self.personalInfo))
#         resume.write(str(experience))
#         resume.write(str(edu_details))
#         resume.write(str(social_media_contact))
#         resume.close()
#         self.say_thanks()
#
#     @classmethod
#     def view_my_resume(cls):
#         logging.info("Jayendran resume is loading...")
#         webbrowser.open("JAYENDRAN_RESUME.txt")
#
#     @classmethod
#     def get_experience(cls):
#         experience = list()
#         experience.append("Currently working as a Software Developer at Zoho Corporation, Chennai")
#         experience.append("Did my QAT internship in Amazon Appstore(Fire TV and Fire Tablets)team at"
#                           " Amazon Development Centre, Chennai")
#         experience.append("Also did an internship of 3 months in Data Analytics and Machine Learning "
#                           "domain at Walinns Analytics India Pvt Ltd,Tidel park:Coimbatore")
#         return experience
#
#     @classmethod
#     def get_educational_details(cls):
#         edu_details = dict()
#         edu_details["Course"] = "B.Tech Information Technology"
#         edu_details["Batch"] = "2015-2019"
#         edu_details["Favorite Subjects"] = "Data structures & Algorithms, Mathematics, AI & ML"
#         return edu_details
#
#     @classmethod
#     def get_social_media_contacts(cls):
#         social_media_contacts = dict()
#         social_media_contacts["LinkedIn"] = "https://www.linkedin.com/in/jayendran-s-194b66122/"
#         social_media_contacts["GitHub"] = "https://github.com/jaijaish98"
#         return social_media_contacts
#
#     def say_thanks(self):
#         print("I'm eagerly waiting for your response to have a discussion with you regarding "
#               "this opportunity")
#         print("Best Regards,")
#         print("{}".format(self.personalInfo["Name: "]))
#         print("{}".format(self.personalInfo["ContactNumber: "]))
#
#
# if __name__ == '__main__':
#     programming_language = "Python 3.X"
#     print("Programming language here I used is {}.".format(programming_language))
#     my_name = "Jayendran S"
#     my_current_location = "Chennai"
#     my_email = "jaijaish98@gmail.com"
#     my_contact_number = "(+91) 996 557 2470"
#     job_application = AmazonSDEJobApplication(my_name, my_current_location, my_email, my_contact_number)
#     job_application.build_resume()
#     job_application.view_my_resume()
#
#
#
#
#
class Vertex:
    def __init__(self, node):
        self.id = node
        ## Mark all nodes unvisited
        self.visited = False
    def addNeighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)
    def gctConnections(self, G):
        return G.adjMatrix(self.id)
    def getVertexID(self):
        return self.id
    def setVertexID(self, id):
        self.id = id
    def setVisited(self):
        self.visited =True
    def __str__(self):
        return str(self.id)

class Graph:

    def __init__(self, numVertices, cost = 0):
        self.adjMatrix = [[0]*numVertices for _ in range(numVertices)]
        self.numVertices =numVertices
        self.vertices = []
        for i in range(0,numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)

    def getVertex(self, n):
        for vertxin in range(0,self.numVertices):
            if n == self.vertices[vertxin].getVertexID():
                return vertxin
		#return -1

    def setVertex(self, vtx, id):
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setVertexID(id)


    def addEdge(self, frm, to, cost= 0):
        if self.getVertex(frm) != - 1 and self.getVertex(to) != - 1:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
            #For directed graph do not add this
            #self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost

    def getVertices(self):
        vertices = []
        for vertxin in range(0,self.numVertices):
            vertices.append(self.vertices[vertxin].getVertexID())
        return vertices

    def printMatrix(self):
        for u in range(0,self.numVertices):
            row= []
            for v in range(0, self.numVertices):
                row.append(self.adjMatrix[u][v])
            print (row)

    def getEdges(self):
        edges= []
        for v in range(0,self.numVertices):
            for u in range(0, self.numVertices):
                if self.adjMatrix[u][v] != 0:
                    vid= self.vertices[u].getVertexID()
                    wid= self.vertices[v].getVertexID()
                    edges.append((vid,wid,1))
        return edges

if __name__ == '__main__':
    G = Graph(5)
    G.setVertex(0,'a')
    G.setVertex(1,'b')
    G.setVertex(2,'c')
    G.setVertex(3,'d')
    G.setVertex(4,'e')
    print ("Graph data:")
    G.addEdge('a', 'e', 10)
    G.addEdge('a', 'c', 20)
    G.addEdge('c', 'b', 30)
    G.addEdge('b', 'e', 40)
    G.addEdge('e', 'd', 50)
    print (G.printMatrix())
    print (G.getEdges())

#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def stringManipulation(s1,s2):
#     if s1==None or s2==None:
#         return "NO"
#     dictionary = {}
#     for i in s1:
#         if i in dictionary:
#             dictionary[i] = dictionary[i]+1
#         else:
#             dictionary[i] = 1
#     for i in s2:
#         if i in dictionary:
#             dictionary[i] = dictionary[i]+1
#         else:
#             dictionary[i] = 1
#     for k,v in dictionary.items():
#         if v%2 == 1:
#             return "NO"
#     return "YES"
#
# tc = int(input())
# for i in range(tc):
#     s1 = input()
#     s2 = input()
#     print(stringManipulation(str(s1),str(s2)))
#
# def tileGame(arr, currPos, result):
#     if len(arr) < 1:
#         return -1
#     if currPos >= len(arr):
#         return result
#     res = [0 for i in range(len(arr))]
#
#     s = len(arr)-1
#     for i in range(s,-1,-1):
#         temp1=arr[i][0]
#         temp2=arr[i][1]
#         temp3=arr[i][2]
#         if i+1<len(arr):
#             temp1 = arr[i][0]+res[i+1]
#         if i+2<len(arr):
#             temp2 = arr[i][1]+res[i+2]
#         if i+3<len(arr):
#             temp3 = arr[i][2]+res[i+3]
#         res[i] = max(temp1,temp2,temp3)
#     return res[0]
#     # res1 = tileGame(arr, currPos + 1, result + arr[currPos][0])
#     # res2 = tileGame(arr, currPos + 2, result + arr[currPos][1])
#     # res3 = tileGame(arr, currPos + 3, result + arr[currPos][2])
#     # return max(res1, res2, res3)
#
# tc = int(input())
# for i in range(tc):
#     arr = []
#     N = int(input())
#     for j in range(N):
#         arr.append(list(map(int, input().split())))
#     print(tileGame(arr,0,0))
