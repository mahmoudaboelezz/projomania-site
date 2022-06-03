

if ( window.history.replaceState ) {
  window.history.replaceState( null, null, window.location.href );
}
if(document.body.contains (category_blog = document.getElementById("profile-info"))){
  document.body.style.backgroundColor = '#e2e8f0'
}
if(document.body.contains (btn = document.querySelector("[data-btn]"))){

btn.onclick = function holyMoly1(event){
  if (form =document.forms[0].checkValidity() == true){
    event.preventDefault();
    btn.classList.add("animating")
    setTimeout(function(){
      document.forms[0].submit();
      },3000)

}}}
// fetch('https://jsonplaceholder.typicode.com/todos')
//   .then(response => response.json())
//   .then(json =>
//     {
//     var array = json;
//     for (let x = 0; x < array.length; x++) {
//       console.log(array[x].title)
      
//     }})

// function popDemo(demoButton) {
//   const demoLink = `<iframe width="400" height="400" class="center" id="youtube" src="https://www.youtube.com/embed/mtm075xWEcU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`

//  demoButton.onclick = function() {
//    if(document.)
//    demoButton.parentNode.append(popDemo)
//  }
// }
function generatePDF() {
  // Choose the element that our invoice is rendered in.
  const element = document.getElementById('invoice');
  // Choose the element and save the PDF for our user.
  html2pdf()
		.set({ html2canvas: { scale: 4 } })
		.from(element)
		.save();
}
function generatePDF1() {
  // Choose the element that our invoice is rendered in.
  const element = document.getElementById('invoice');
  const title = document.getElementById('issueTitle');
  var data = document.createElement('div');
  data.appendChild(title.cloneNode(true)); 
  data.appendChild(element.cloneNode(true)); 
  var opt = {
    margin:       1,
    filename:     title.innerText,
    image:        { type: 'jpeg', quality: 0.98 },
    html2canvas:  { scale: 2 },
  jsPDF:        { unit: 'in', format: 'letter', orientation: 'landscape' }
    // 
  };
  
  // New Promise-based usage:
  html2pdf().set(opt).from(data).save();
}


document.addEventListener("DOMContentLoaded", function() {
  let setAll0 = document.querySelectorAll("#id_category");
  let setAll1 = document.querySelectorAll("#id_comapnyCountry");
  let setAll2 = document.querySelectorAll("#id_author");

  if(document.body.contains (category_blog = document.getElementById("id_category"))){
    setAll0[0].options[0].textContent = "All"
    category_blog.addEventListener("change", autosubmit);

    if(document.body.contains(category_author = document.getElementById("id_author"))){
      setAll2[0].options[0].textContent = "All"
    category_author.addEventListener("change", autosubmit);}

    if(document.body.contains(comapnyCountry = document.getElementById("id_comapnyCountry"))){
      setAll1[0].options[0].textContent = "All"
      comapnyCountry.addEventListener("change", autosubmit);}
    form = document.getElementById('seachbyselect')
    function autosubmit() {
      form.submit()
    }
    
    // resetButton.addEventListener('click', function clearSearch(){
      
      // })
      
      
      
      
      
    }
    if(document.body.contains (resetButton = document.getElementById("reset"))){
      resetButton.addEventListener('click', () => window.location.search = "")
    }
  if(document.body.contains(document.getElementById("swipe"))){
    
    document.getElementById('header').setAttribute("style", "min-height: 24rem;");
  }
  if(document.body.contains(document.getElementById("ticketh2"))){
  
    document.getElementById('mainsec').setAttribute("style", "min-height: 1px;");
    document.getElementById('footer').setAttribute("style", "margin-top: 10px;");
  }
  

});
// 
// if(document.body.contains(document.getElementById("ff")))
// {
//   var a = document.getElementById("ff");
//   a.onsubmit = location.replace("")
// }


// function redirect(){
//   window.location.href = "";
// }
if(document.body.contains(document.getElementById("loginpic"))){
  // document.getElementById('header').setAttribute("style", "display: none;");
  document.getElementById('footer').setAttribute("style", "display: none;");
  //document.body.setAttribute("style", "background-color: #eee;");

}



if(document.body.contains(document.getElementById("contact")))
{
  contact = document.getElementById("rom");
  book = document.getElementById("second");
  book.style.display="none";
  contact.style.display="none";
  loadbefore = document.querySelector("#sp1");
  loadafter = document.querySelector("#sp2");

  document.getElementById("show-contact").onclick = function(){
    book.style.display="none";
    document.getElementById("show-book").style.removeProperty("backgroundColor");
    document.getElementById("show-contact").style.removeProperty("backgroundColor");

    if(contact.style.display==="revert"){
      contact.style.display="none";
      document.getElementById("show-contact").style.backgroundColor = "#999999"

    }
    else{
      loadbefore.style.cssText="animation-play-state: running; display:revert;"
      loadbefore.addEventListener("animationend",() =>{
      loadbefore.style.cssText="display:none;"
      contact.style.display="revert";
      document.getElementById("show-contact").style.backgroundColor = "#0ED4A8"
      
    })
      
  }
    }

  
  document.getElementById("show-book").onclick = function(){
    contact.style.display="none";
    
    
    document.getElementById("show-book").style.backgroundColor = "#999999"
    document.getElementById("show-contact").style.backgroundColor = "#999999"

    if(book.style.display==="revert"){
      book.style.display="none";
      document.getElementById("show-book").style.backgroundColor = "#999999"
    }
    else{
      loadafter.style.cssText="animation-play-state: running; display:revert;"
      loadafter.addEventListener("animationend",() =>{     book.style.display="revert";
      document.getElementById("show-book").style.backgroundColor = "#0ED4A8"
      loadafter.style.cssText="display:none;"
    })
 
  }
  }
}








// if(document.body.contains(document.getElementById("ff")))
// {
//   document.getElementById('header').setAttribute("style", "min-height: 250px;");}


if(document.body.contains(document.getElementById("firstOne")))
{
  document.getElementById('header').setAttribute("style", "min-height: 250px;");


}


function update() {
  var select = document.getElementById("services");
  var option = select.options[select.selectedIndex];
  

  //document.getElementById('value').value = option.value;
  if(document.body.contains(document.getElementById("id_mainService"))){
    document.getElementById(
      "id_mainService"
    ).value = `Odoo Version : ${option.text}`;
  }

}


function formFunction() {
  var text = document.createElement("input");
  text.type = "text";
  text.id = "id_mainService";
  text.name = "mainService";

  text.setAttribute("readonly", true);
  var parent = document.getElementById("appending");
  parent.appendChild(text);
  var moreService = `<div class='selectBox'> <ul id="id_my_field">
  <li><label for="id_my_field_0"><input type="checkbox" name="my_field" value="ODOO DEVELOPMENT" id="id_my_field_0">
ODOO DEVELOPMENT</label>

</li>
  <li><label for="id_my_field_1"><input type="checkbox" name="my_field" value="CODE UPGRADING" id="id_my_field_1">
CODE UPGRADING</label>

</li>
  <li><label for="id_my_field_2"><input type="checkbox" name="my_field" value="DATABASE MIGRATION" id="id_my_field_2">
DATABASE MIGRATION</label>

</li>
  <li><label for="id_my_field_3"><input type="checkbox" name="my_field" value="LINUX ADMINISTRATION" id="id_my_field_3">
LINUX ADMINISTRATION</label>

</li>
</ul> </div>`;

  var more = document.createElement("div");
  more.className = "moreServices";
  more.innerHTML = moreService;
  parent.append(more);

  var emptyDiv = document.createElement("div");
  parent.appendChild(emptyDiv);

  var buttonmore = document.createElement("button");
  buttonmore.className = "btn btn btn-secondary";
  buttonmore.id = "addmore"
  buttonmore.innerHTML = "Select a plan";

  parent.appendChild(buttonmore);
  var emailField = document.createElement("input");
  emailField.type = "email";
  emailField.name = "email";
  emailField.id = "id_email";
  emailField.ariaLabel = "Main";
  parent.appendChild(emailField);
  emailField.placeholder ="Your Email to book the service";

  var butn = document.getElementById("btun");
  butn.className = "center";
  butn.parentNode.removeChild(butn);

  var buttonCancel = document.createElement("button");
  buttonCancel.className = "btn btn-primary";
  buttonCancel.innerHTML = "Cancel";
  buttonCancel.id = "cancel";

  var buttonBook = document.createElement("button");
  buttonBook.className = "btn btn-primary";
  buttonBook.innerHTML = "Book";
  buttonBook.type = "submit";
  buttonBook.name ='btnform1';
  buttonBook.id = "bookSubmit";
  // buttonBook.setAttribute("onsubmit","return false")

  var freeSpan = document.createElement("span");
  

  parent.appendChild(buttonCancel);
  parent.appendChild(buttonBook);
  parent.appendChild(freeSpan);

  update();


 
  document.getElementById("bookSubmit").onmouseenter =  function(event) {
    let matches = document.querySelectorAll('input[type=checkbox]:checked');
    let a = document.getElementById("bookSubmit");
    let word = document.createElement("h6");
  
    word.className = "alert alert-danger";
    
  
    if (matches.length < 1) {
      
      a.setAttribute("disabled",true);
      word.innerText = "Please select at least 1 service";
      
      //word.style.cssText = "color: red;"
      emptyDiv.appendChild(word);
      

      setTimeout(function() {
        a.removeAttribute("disabled")
        setTimeout(function() {
          word.parentNode.removeChild(word)
          
        }, 2000);
      }, 3000);
      return false;
    }
    //check if there is no email
    else if (emailField.value.length == 0) {

      word.innerText = "Enter a Valid Email";
      //emailField.parentNode.appendChild(word)
      // freeSpan.appendChild(word);
      emailField.after(word)
      a.setAttribute("disabled",true);

      setTimeout(function() {
        a.removeAttribute("disabled")
        setTimeout(function() {
          word.parentNode.removeChild(word)
          
        }, 2000);
      }, 3000);
      return false;
    }
    
   };
   buttonBook.onclick =function holyMoly(event){
    event.preventDefault();
    Swal.fire(
      'Thanks For Booking..',
      'We will contact you as soon as possible!',
      'success'
    )
    setTimeout(function(){
  document.forms[1].submit();
    },4000)

   }

  //  const btn = document.querySelector("[data-btn]")
  //  btn.addEventListener("click", () => {
  //    btn.classList.add("animating")
     
  //  })

  buttonmore.onclick = function () {
    buttonmore.parentNode.removeChild(buttonmore);
    var specialOrder = document.createElement("input");
    specialOrder.type = "text";
    specialOrder.id = "id_SpecialOrder"
    specialOrder.name = 'SpecialOrder';
    specialOrder.placeholder = "1M record...";
    var db = document.createElement("h6");
    db.innerHTML = "<br>Please type the DB size"
    emptyDiv.appendChild(db);
    emptyDiv.appendChild(specialOrder);
  
  };
  buttonCancel.onclick = function () {
    
    emailField.parentNode.removeChild(emailField);
    text.parentNode.removeChild(text);
    buttonBook.parentNode.removeChild(buttonBook);
    buttonCancel.parentNode.removeChild(buttonCancel);
    parent.appendChild(butn);
    if(!!document.getElementById("addmore") === true){
      parent.removeChild(buttonmore);
    
    }
    else if(!!document.getElementById("specialOrder") === true){
      specialOrder.parentNode.removeChild(specialOrder);
    }
    more.parentNode.removeChild(more);
    
    



  };
}
if ( window.history.replaceState ) {
  window.history.replaceState( null, null, window.location.href );
}

// if(document.body.contains(document.getElementById("id_mainService"))){
// document.getElementById("send").onclick =function holyMoly1(event){


//   setTimeout(function(){
//     event.stopPropagation();
//     console.log("test1")
    

//   },4000)}}


// function categoryAll(){
  
//   categoryAll1.forEach(function(ele)
//   {
// ele.textContent.replace("---------","all");
// });

// }
// window.onload = categoryAll;
// function callabal(){
//   document.addEventListener('DOMContentLoaded', function() {
//     let categoryAll1 = document.querySelectorAll("#id_category");
//     categoryAll1.forEach(function(ele)
//       {
//     a = ele.textContent.replace("---------","all");
//     console.log(a)
//     });
    
//   });
// }

// callabal();
