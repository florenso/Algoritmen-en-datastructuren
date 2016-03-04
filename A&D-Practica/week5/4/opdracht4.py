import time

INFINITY = float("inf")
class myqueue( list):

    def enqueue(self,s):
        self.append(s)

    def dequeue(self):
        return self.pop(0)


class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self): # voor afdrukken
        return str(self.data)

    def __lt__(self, other): # voor sorteren
        return self.data < other.data
def vertices(G):
    a = list(G.keys())
    a.sort()
    return a

def edges(G):
    a = []
    for u in vertices(G):
        for v in G[u]:
            a.append((u,v))
    return a

def keerOm(G):
    r = {}
    for dummy in vertices(G):
        r[dummy]=[]
        pass
    tmp = edges(G)
    for a,b in tmp:
        list = r.get(b)
        list.append(a)
        r[b]=list
        pass
    print("succes")
    return r

# 1 = opgave 1.1
# 2 = opgave 1.2
# 3 = opgave 2.1
# 4 = opgave 3.1
# 5 = opgave 4.1
# 6 = opgave 4.2
# 7 = opgave 5.1
graaf = 1
G=None
v=None
if graaf == 1:
    #eerste graaf
    v = [Vertex(i) for i in range(8)]
    G = {v[0]:[v[4],v[5]],
         v[1]:[v[4],v[5],v[6]],
         v[2]:[v[4],v[5],v[6]],
         v[3]:[v[7]],
         v[4]:[v[0],v[1],v[2],v[5]],
         v[5]:[v[4],v[0],v[1],v[2]],
         v[6]:[v[1],v[2]],
         v[7]:[v[3]]}
elif graaf ==2:
    #tweede graaf
    v = [Vertex(i) for i in range(7)]
    G = {v[0]:[v[4],v[5]],
         v[1]:[v[4],v[5],v[6]],
         v[2]:[v[4],v[5],v[6]],
         #v[3]:[],
         v[4]:[v[0],v[1],v[2],v[5]],
         v[5]:[v[4],v[0],v[1],v[2]],
         v[6]:[v[1],v[2]]}

elif graaf ==3:
    v = [Vertex(i) for i in range(8)]
    G = {
    v[0]:[v[5],v[4]],
    v[1]:[v[4],v[6]],
    v[2]:[v[5]],
    v[3]:[v[7]],
    v[4]:[v[0],v[1]],
    v[5]:[v[0],v[2]],
    v[6]:[v[1]],
    v[7]:[v[3]]
    }
elif graaf ==4:
    v = [Vertex(i) for i in range(8)]
    G = {
    v[0]:[v[1],v[3]],
    v[1]:[v[0],v[2]],
    v[2]:[v[1],v[4],v[3]],
    v[3]:[v[0],v[2]],
    v[4]:[v[2],v[5],v[6]],
    v[5]:[v[4],v[6]],
    v[6]:[v[4],v[5],v[7]],
    v[7]:[v[6]]
    }
elif graaf ==5:
    v = [Vertex(i) for i in range(3)]
    G = {
    v[0]:[v[1]],
    v[1]:[v[2]],
    v[2]:[v[0]],
    }
elif graaf ==6:
    v = [Vertex(i) for i in range(3)]
    G = {
    v[0]:[v[1]],
    v[1]:[],
    v[2]:[v[0],v[1]],
    }
elif graaf ==7:
    v = [Vertex(i) for i in range(8)]
    G = {
    v[0]:[v[1],v[2]],
    v[1]:[v[0],v[3]],
    v[2]:[v[0],v[3]],
    v[3]:[v[1],v[2],v[4],v[6]],
    v[4]:[v[5],v[7],v[6],v[3]],
    v[5]:[v[4],v[6]],
    v[6]:[v[3],v[4],v[5],v[7]],
    v[7]:[v[6],v[4]]
    }

print("vertices(G):",vertices(G))
print("edges(G):",edges(G))

def show_tree_info(G):
    print('tree:', end = ' ')
    for v in vertices(G):
        print('(' + str(v), end = '')
        if hasattr(v,'distance'):
            print(',d:' + str(v.distance), end = '')
        if hasattr(v,'predecessor'):
            print(',p:' + str(v.predecessor), end = '')
        print(')', end = ' ')
    print()

show_tree_info(G)

def is_strongly_connected_med1(G):

    V = vertices(G)
    #s=V[0]
    for s in V:
        s.predecessor = None # s krijgt het attribuut 'predecessor'
        s.distance = 0 # s krijgt het attribuut 'distance'
        for v in V:
            if v != s:
                v.distance = INFINITY # v krijgt het attribuut 'distance'
        q = myqueue()
        q.enqueue(s) # plaats de startnode in de queue
        while q:
            u = q.dequeue()
            for v in G[u]:
                if v.distance == INFINITY: # v is nog niet bezocht
                    v.distance = u.distance + 1
                    v.predecessor = u # v krijgt het attribuut 'predecessor'
                    q.enqueue(v) # plaats de buren van v in de queue
        for dummy in V:
            if dummy.distance== INFINITY:
                return False
    return True

def is_strongly_connected(G,re=False):

    V = vertices(G)
    s=V[0]
    #for s in V:
    s.predecessor = None # s krijgt het attribuut 'predecessor'
    s.distance = 0 # s krijgt het attribuut 'distance'
    for v in V:
        if v != s:
            v.distance = INFINITY # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s) # plaats de startnode in de queue
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY: # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u # v krijgt het attribuut 'predecessor'
                q.enqueue(v) # plaats de buren van v in de queue
    for dummy in V:
        if dummy.distance== INFINITY:
            return False
    if re == True and is_strongly_connected(keerOm(G),True) == False :
        return False
    return True


start = time.clock()
print("strong 1:",is_strongly_connected_med1(G))
elapsed = time.clock()
elapsed = elapsed - start
print("Time spent in (function name) is: ", elapsed)

start = time.clock()
print("strong 2:",is_strongly_connected(G))
elapsed = time.clock()
elapsed = elapsed - start
print("Time spent in (function name) is: ", elapsed)


#print(edges(G))
#print(edges(keerOm(G)))