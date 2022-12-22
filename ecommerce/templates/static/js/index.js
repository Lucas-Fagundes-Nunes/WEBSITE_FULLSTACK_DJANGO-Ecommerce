user = document.getElementById('divUser');

function openDivUser(valor)
{
    if(valor == 1)
    {

        user.style.opacity=1
        user.style.display='block'
      

    }else
    {
        user.style.display='none'
        user.style.opacity=0
    }
}

function horarioAtual() {
    user.style.opacity= 0
    user.style.display='none'

  
  }
  
  setInterval(horarioAtual, 6000);