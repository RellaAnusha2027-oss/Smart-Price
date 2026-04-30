
<!-- your whole HTML above -->

<script>
  function predict(){
    let area = parseFloat(document.getElementById("area").value);
    let bed = parseFloat(document.getElementById("bed").value);
    let bath = parseFloat(document.getElementById("bath").value);
    let loc = parseFloat(document.getElementById("location").value);

    if(!area || !bed || !bath || !loc){
      document.getElementById("result").innerHTML = "⚠️ Fill all fields!";
      return;
    }

    let price = (area * 2000) + (bed * 50000) + (bath * 30000) + (loc * 10000);

    document.getElementById("result").innerHTML =
      "💰 Estimated Price: ₹ " + price.toLocaleString();
  }
</script>

</body>
</html>
