from locationField import Location, Field
from drunkardsWalk import Walk,simWalks,drunkTest
from iteratingStyles import styleIterator
from usualAndUnusual import Drunk, usualDrunk
from biasedRandomWalk import coldDrunk, ewDrunk
from plottingWalks import plotRandomWalks
from plottingWalks import simAll1

simAll1((usualDrunk,coldDrunk,ewDrunk),(10,100,1000),1000)
