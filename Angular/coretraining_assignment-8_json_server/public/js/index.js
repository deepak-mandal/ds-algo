//Function to View Record
function viewData(){
    var ActionOnId=document.getElementById("inputField").value;
    fetch('http://localhost:3000/dept?id='+ActionOnId)
    .then(res=>{
        if(res.ok){
            //alert("Successfully read the data");
        }
        else{
            console.log("Error getting the data");
        }
        return res.json()

    })
    .then(dept => {
        alert("ID: "+dept[0].id+"\nDepartment name: "+dept[0].deptname+"\nLocation: "+dept[0].location);
    })
    .catch(error=>console.log(error))

}


//Function to delete the existing records
function deleteData(){
    var ActionOnId=document.getElementById("inputField").value;
    fetch('http://localhost:3000/dept/'+ActionOnId, {
        method: 'Delete',
        headers:{
            "Content-Type":"application/json"
        }
        
    })

}


//To fetch and display data in HTML tabular form in Dynamic way
fetch("http://localhost:3000/dept/")
.then(res => {
    res.json().then(
        data => {
            console.log(data);
            if(data.length >0){
                var temp="";

                data.forEach((u) => {
                    temp+="<tr>";
                    temp+="<td>"+u.id+"</td>";
                    temp+="<td>"+u.deptname+"</td>";
                    temp+="<td>"+u.location+"</td>";
                })

                document.getElementById("fillData").innerHTML = temp;

            }
        }
    )
})





//Function to Insert Data
function insertData(){
    var ActionOnId=document.getElementById("inputId").value;
    var ActionOnDeptName=document.getElementById("inputDeptName").value;
    var ActionOnLocation=document.getElementById("inputLoc").value;
    var dept={
        "id":ActionOnId,
        "deptname":ActionOnDeptName,
        "location":ActionOnLocation
    }

    fetch('http://localhost:3000/dept', {
        method:'POST',
        headers:{
            "Content-Type" : "application/json"
        },
        body:JSON.stringify(dept)

    })
    .then(res => console.log(res));


}



//Function to update Records
function updateData(){
    /*
    var dept = {
        "id":"121",
        "deptname":"Home",
        "location":"Earth"
    }
    */
    var ActionOnId=document.getElementById("inputId").value;
    var ActionOnDeptName=document.getElementById("inputDeptName").value;
    var ActionOnLocation=document.getElementById("inputLoc").value;
    var dept={
        "id":ActionOnId,
        "deptname":ActionOnDeptName,
        "location":ActionOnLocation
    }

    //console.log(ActionOnLocation);
    
    fetch('http://localhost:3000/dept/'+ActionOnId, {
        method:'PUT',
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(dept)
    })
    .then(res => console.log(res))
    
}


