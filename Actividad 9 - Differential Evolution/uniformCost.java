expandedNodes = new ArrayList<PathManualTree.Node>();
visitedNodes = new HashSet<>(225);	//Explored in Wiki pseudocode.

HeuristicPathTree.Node actualNode = nodes[initialY][initialX];
float solutionPathCost = 0;
expandedNodes.add(actualNode);	//Frontier in Wiki pseudocode.
boolean found = false;

setAdyacentFieldsAndColor(initialY, initialX);

do{
	if(expandedNodes.isEmpty()){
		//return failure???
	}
	actualNode = expandedNodes.poll();
	visitedNodes.add(actualNode);

	if(isFinal(finalY, finalX)){
		found = true;
	}

	for(String direction : expansionOrder){
		HeuristicPathTree.Node neighborNode;
		float cost;
		if(direction == "UP"){
			neighborNode = nodes[actualY-1][actualX];
			cost = neighborNode.getAccumulative();
			if(!visitedNodes.contains(neighborNode)){
				if(!expandedNodes.contains(neighborNode)){
					neighborNode.setAccumulative = actualNode.getAccumulative() + cost();
					expandedNodes.add(neighborNode);
					setAdyacentFieldsAndColor(initialY-1, initialX);
				}
				else if(expandedNodes.get(neighborNode.getAccumulative()) > (actualNode.getAccumulative() + cost)){
					neighborNode.setAccumulative(actualNode.getAccumulative() + cost);
					expandedNodes.remove(neighborNode);
					expandedNodes.add(neighborNode);
				}
			}
		}
		else if(direction == "DOWN"){
			neighborNode = nodes[actualY+1][actualX];
			if(!visitedNodes.contains(neighborNode)){
				if(!expandedNodes.contains(neighborNode)){
					neighborNode.setAccumulative = actualNode.getAccumulative() + cost();
					expandedNodes.add(neighborNode);
					setAdyacentFieldsAndColor(initialY+1, initialX);
				}
				else if(expandedNodes.get(neighborNode.getAccumulative()) > (actualNode.getAccumulative() + cost)){
					neighborNode.setAccumulative(actualNode.getAccumulative() + cost);
					expandedNodes.remove(neighborNode);
					expandedNodes.add(neighborNode);
				}
			}
		}
		else if(direction == "LEFT"){
			neighborNode = nodes[actualY][actualX-1];
			if(!visitedNodes.contains(neighborNode)){
				if(!expandedNodes.contains(neighborNode)){
					neighborNode.setAccumulative = actualNode.getAccumulative() + cost();
					expandedNodes.add(neighborNode);
					setAdyacentFieldsAndColor(initialY, initialX-1);
				}
				else if(expandedNodes.get(neighborNode.getAccumulative()) > (actualNode.getAccumulative() + cost)){
					neighborNode.setAccumulative(actualNode.getAccumulative() + cost);
					expandedNodes.remove(neighborNode);
					expandedNodes.add(neighborNode);
				}
			}
		}
		else if(direction == "RIGHT"){
			neighborNode = nodes[actualY][actualX+1];
			if(!visitedNodes.contains(neighborNode)){
				if(!expandedNodes.contains(neighborNode)){
					neighborNode.setAccumulative = actualNode.getAccumulative() + cost();
					expandedNodes.add(neighborNode);
					setAdyacentFieldsAndColor(initialY, initialX+1);
				}
				else if(expandedNodes.get(neighborNode.getAccumulative()) > (actualNode.getAccumulative() + cost)){
					neighborNode.setAccumulative(actualNode.getAccumulative() + cost);
					expandedNodes.remove(neighborNode);
					expandedNodes.add(neighborNode);
				}
			}
		}
	}
}while(!expandedNodes.isEmpty() && found == false);