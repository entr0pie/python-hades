async function getSession() {
    const response = await fetch("/session");
    return response.json();
}

function readNodes(raw_nodes) {
    let nodes = [];
    
    for (let i = 0; i < raw_nodes.length; i++) {
        const id = i + 1; 
        const element_id = raw_nodes[i].element_id;
        const name = raw_nodes[i].properties.name;
        const labels = raw_nodes[i].labels;
        const properties = raw_nodes[i].properties;

        nodes.push({
            id: id,
            element_id: element_id,
            label: name,
            labels: labels,
            properties: properties
        });
    }

    return nodes;
}

function readEdges(nodes, raw_edges) {
    let edges = [];
    
    for (let i = 0; i < raw_edges.length; i++) {
        const [left_element_id, raw_element_id] = raw_edges[i].nodes;        
        let [left_id, right_id] = [0, 0];
        
        for (let j = 0; j < nodes.length; j++) {
            if (left_element_id == nodes[j].element_id) {
                left_id = nodes[j].id;
            } else if (raw_element_id == nodes[j].element_id) {
                right_id = nodes[j].id;
            } 
        }

        edges.push( {from: left_id, to: right_id });
    }

    return edges;
}

async function main() {
    const graph = await getSession();
    let nodes = readNodes(graph.nodes);
    
    for (let i = 0; i < nodes.length; i++) {
        if (nodes[i].label == "Host") {
            nodes[i].color = "#DE1502";
        }
    }
    
    
    let edges = readEdges(nodes, graph.edges);
    
    nodes = new vis.DataSet(nodes);
    edges = new vis.DataSet(edges);

    var container = document.getElementById('mynetwork');

    var data = {
        nodes: nodes,
        edges: edges
    };
    
    var options = {
        nodes: {
            font: { size: 12, color: '#FFFFFF', face: 'arial' },
            shape: "dot",
            size: 10
        },

        edges: {
            smooth: false
        }
    };
    var network = new vis.Network(container, data, options);
}

main();