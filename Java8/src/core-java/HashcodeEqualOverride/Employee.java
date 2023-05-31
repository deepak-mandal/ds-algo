public class Employee{
    private int id;
    private String name;

    //getter and setter, and constructur

    @Override
    public int hashCode(){
        return id%7;
    }


    @Override
    public boolean equals(Object o){
        Employee e = (Employee) o;
        if(this.id==e.id){
            return true;
        }
        else {
            return false;
        }
    }


    @Override
    public String toString(){
        return "Id = "+ id+"...";
    }
}