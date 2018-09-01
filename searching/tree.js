// https://code.tutsplus.com/articles/data-structures-with-javascript-tree--cms-23393
export class Node {
    constructor(data){
        this.data = data;        
        this.parent = null;
        this.children = [];
    }
}


export default class Tree {
    constructor(data){
        this._root = new Node(data);
    }

    contains(callback, traversal){
        traversal.call(this,callback);
    }

    add(data, toData, traversal){
        let child = new Node(data),
            parent = null,
            callback = function(node) {
                if (node.data === toData) {
                    parent = node;
                }
            };

        this.contains(callback, traversal);

        if (parent) {
            parent.children.push(child);
            child.parent = parent;
        } else {
            throw new Error('Cannot add node to a non-existent parent.');
        } 
    }
}
