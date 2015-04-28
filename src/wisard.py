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

Wisard e uma implementacao de rede neural sem peso.
"""
RND = 3141


def wirer(retina):
    return [(retina.pop(RND % len(retina)), retina.pop(RND % len(retina))) for _ in range(len(retina)//2)]


def tupler(x):
    return [(bit,)+tup for bit in (0, 1) for tup in tupler(x-1)] if x else [(0,), (1,)]


class Wisard:
    """Rede neural sem peso. :ref:`wisard'
    """
    def __init__(self, retinasize=3*4, ramorder=2):
        self.cortex = [{t: 0 for t in tupler(ramorder-1)} for _ in range(retinasize//2)]

    def learn(self, retina):
        [self.cortex[ram].update({(retina.pop(RND % len(retina)), retina.pop(RND % len(retina))): 1})
         for ram in range(len(retina)//2)]

    def classify(self, retina):
        return sum([self.cortex[ram][(retina.pop(RND % len(retina)), retina.pop(RND % len(retina)))]
                    for ram in range(len(retina)//2)])


def main():
    print('Wisard 0.1.0')
    print(tupler(1))
    print(wirer(list(range(12))))
    print(wirer(list(range(12))))
    wis = Wisard()
    print(wis.cortex)
    wis.learn([1, 0, 0, 1]+[1, 1, 1, 1]+[1, 0, 0, 1])
    print(wis.cortex)
    print(wis.classify([1, 0, 0, 1]+[1, 1, 1, 1]+[1, 0, 0, 1]))
    print(wis.classify([1, 0, 0, 1]+[1, 1, 1, 1]+[1, 0, 0, 1]))

main()
