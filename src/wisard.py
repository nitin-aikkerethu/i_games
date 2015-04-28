"""
############################################################
Wisard - Principal
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2015/04/08
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2015, `GPL <http://is.gd/3Udt>`__.

Wisard e uma impplementacao de rede sem peso.
"""
RND = 3141
def wirer(retina):
    return [(retina.pop(RND % len(retina)), retina.pop(RND % len(retina))) for t in range(len(retina)//2)]

def tupler(x):
    return [(bit,)+tup for bit in (0,1) for tup in tupler(x-1)] if x else [(0,),(1,)]


class Wisard:
    """Rede neural sem peso. :ref:`wisard'
    """
    def __init__(self, rx=4,  ry=3, discriminators=3, ramorder=2):
        self.cortex = [{t:0 for t in tupler(ramorder-1)}]* discriminators
    def learn(retina):
        [self.cortex[(retina.pop(RND % len(retina)), retina.pop(RND % len(retina)))].put(1)
         for t in range(len(retina)//2)]
    def classify(bitvector):
        return sun([self.cortex[(retina.pop(RND % len(retina)), retina.pop(RND % len(retina)))]
        	 for t in range(len(retina)//2)])


def main():
    print('Wisard 0.1.0')
    print(tupler(1))
    print(wirer(list(range(20))))
    print(wirer(list(range(20))))
    
main()
