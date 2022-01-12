package main
import (
  "fmt"
  "testing"
  "math/rand"
  "math"

)

func TestInsert(test *testing.T) {
  var te avl_tree
  min := 0
  max := 5000000
  tree_size := []int{100, 1000, 5000, 10000}
  values := []int{}
  //build 4 trees of diferent sizes and test if their height is right
  for t:=3; t>=0; t-- {

  for i:=0; i<tree_size[t]; i=i+1 {
    random := rand.Intn(max - min) + min
    //eliminate repeated numbers
    for e:=0; e < len(values) ; e++ {
      if random == e {
        random = rand.Intn(max - min) + min
        e = 0
      }
    }
    values = append(values, random)
    te.insert(random)
  }
  //check if our tree has the height required
  if float64(te.root.get_height()) > math.Log2(float64(tree_size[t]))*1.44{
    test.Errorf("something is wrong")
  } else{
    fmt.Printf("tree of %d nodes is avl \n", tree_size[t])
  }
  //reset the tree
  te.root = nil
}


}
