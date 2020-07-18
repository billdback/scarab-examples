# scarab-examples
This package contains example projects using the scarab simultion.  
The goal is twofold.  First, provide examples of how to create simulations.  Second
use these examples as drivers for improvement and testing of the framework.  

## Beehive
The beehive example is a very basic beehive that controls the hive temperature by bees
"fanning" to cool or "buzzing" to warm the hive to keep it in an acceptable range.  
This simple simulation demonstrates how to create simple entities and tie them together as
part of a simulation.  Note that these fundamentals will be used in all simulations.

The beehive simulation demonstrated emergent behaviors.  The bees all have different tolerances
for heat and will start fanning and buzzing in different ranges.  By varying to make the bees
all the same or different, you can see sharp changes vs. gradual changes in the temperature. 

