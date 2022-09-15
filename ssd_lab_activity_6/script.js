
        function validate() {
          
          var name = document.getElementById("username").value;
        document.write(name);
          //do checking here however you like (regex, iteration, etc.)
          var letterNumber = /^[0-9a-zA-Z]+$/;

          if(name.match(letterNumber)) 
          {
            
          return true;
          }
          else
          { 
            
          alert("Invalid Username"); 
          return false; 
          }
      }
