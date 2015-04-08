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


class Wisard:
    """Uma caverna com cameras tuneis e habitantes. :ref:`caverna`
    """
    def __init__(self, rx=16,  ry=16, dis=2, ramorder=2):
        """Initializes builder and gui. """
        rx,  ry, dis, ramorder  = rx,  ry, dis, ramorder
        wiring = shuffle(range(rx*ry))
        discriminators = [Discriminator() for d in range(dis)]


def main(gui):
    print('Caverna 0.1.0')
    caverna = Wisard()
