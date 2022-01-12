package main
import (
  "fmt"
)

type node struct{
  val int
  times int // => saves how many times a key has been saved
  height int
  right *node
  left *node
}

type avl_tree struct{
  root *node
}

func get_max(x int, y int) int {
  if x > y {

    return x

  } else{

    return y
  }
}

func (tree *avl_tree) right_rotation(x *node, x_parent *node){
  if x_parent == nil {
    temp := x.left
    x.left = temp.right
    temp.right = x
    tree.root = temp

  } else if x == x_parent.left  {
    temp := x.left
    x_parent.left = temp
    x.left = temp.right
    temp.right = x

  } else {
    temp := x.left
    x_parent.right = temp
    x.left = temp.right
    temp.right = x
  }
}

func (tree_node *node) get_height() int{
  if tree_node == nil{
    return -1
  }

  return 1+ get_max(tree_node.left.get_height(), tree_node.right.get_height())
}

func (tree_node *node) get_delta_height() int{

  r := tree_node.right.get_height()
  l := tree_node.left.get_height()

  return l - r

}

func (tree *avl_tree) left_rotation (x *node, x_parent *node) {
  if x_parent == nil {
    temp := x.right
    x.right = temp.left
    temp.left = x
    tree.root = temp

  } else if x == x_parent.left  {
    temp := x.right
    x_parent.left = temp
    x.right = temp.left
    temp.left = x

  } else {
    temp := x.right
    x_parent.right = temp
    x.right = temp.left
    temp.left = x
  }
}

// meant to be called ONLY after inserting one node
func (tree *avl_tree) balance (nodes []*node){

  for e := len(nodes)-1; e >= 0; e-- {
    //if our three is heavy on the left
    if nodes[e].get_delta_height() == 2 {

      if nodes[e].left.get_delta_height() == -2{
        tree.left_rotation(nodes[e].left, nodes[e])

        if e == 0 {
          tree.right_rotation(nodes[e], nil)

        } else{
          tree.right_rotation(nodes[e], nodes[e-1])
        }

      } else {

        if e == 0 {
          tree.right_rotation(nodes[e], nil)

        } else{
          tree.right_rotation(nodes[e], nodes[e-1])
        }
        }
    }
    //if our three is heavy on the right
    if nodes[e].get_delta_height() == -2 {

      if nodes[e].right.get_delta_height() == 2 {
        tree.right_rotation(nodes[e].right, nodes[e])

        if e == 0 {
          tree.left_rotation(nodes[e], nil)

        } else{
          tree.left_rotation(nodes[e], nodes[e-1])
        }

      } else {

        if e == 0 {
          tree.left_rotation(nodes[e], nil)

        } else{
          tree.left_rotation(nodes[e], nodes[e-1])
        }
        }
    }
	}
}

func (r *avl_tree) lookup (val int) *node{

  cur := r.root

  for cur != nil {

    if cur.val == val {
      return cur

    } else if cur.val > val {

      cur = cur.left

    } else if cur.val < val {

      cur = cur.right
    }
  }
  return nil
}

// Inserts node and balances the three, returns a boolean indicating success.
func (r *avl_tree) insert (val int) bool {
  //On an empty tree, it adds the first node
  var n node
  n.val, n.height, n.times = val, 0, 1

  if r.root == nil {
    //????
    //does this allocate n to be used everywhere as long as
    //r.root is still alive
    // var n node
    // n.val, n.height, n.times = val, 0, 1
    r.root = &n
    return true
  }
 //The nodes that will be iterated are the ones that will have their heights changed
 //so they are going to be saved in a list

 nodes := []*node{r.root} //????this has to change to the height eventually
 cur := r.root

 for cur != nil{

   if cur.val < val {

     if cur.right == nil {
       cur.right = &n
       r.balance(nodes)

       return true
     }

     nodes = append(nodes, cur.right)
     cur = cur.right

   } else if cur.val > val {

     if cur.left == nil {
       cur.left = &n
       r.balance(nodes)

       return true
     }

     nodes = append(nodes, cur.left)
     cur = cur.left

   } else if cur.val == val {

     cur.times = cur.times + 1
     return true

   }
 }
  return false
}

func main(){
  var h avl_tree
  h.insert(100)

  h.insert(101)
  h.insert(101)
  h.insert(105)
  fmt.Printf("%d", h.root.get_height())

}
