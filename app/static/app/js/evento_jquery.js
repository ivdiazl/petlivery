$(document).ready(function(){
    

    $("#sumar2").click(
        function(){
            var elec = $("#eleccion1").val();
            var desc = $("#descuento").val();
            

            if(elec == "promo1" && desc == "ivan" ){
                var promo1 = 250 
                $("#total").val(promo1)
            }else if (elec == "promo1"){
                var promo1 = 500 
                $("#total").val(promo1)
            }else if (elec == "promo2" && desc == "ivan" ){
                var promo1 = 150 
                $("#total").val(promo1)
            }else if (elec == "promo2"){
                var promo2 = 300 
                $("#total").val(promo2)
            }else if (elec == "promo3" && desc == "ivan" ){
                var promo3 = 200 
                $("#total").val(promo3)
            }else if (elec == "promo3"){
                var promo3 = 400 
                $("#total").val(promo3)
            }else if (elec == "promo4" && desc == "ivan"){
                var promo4 = 300 
                $("#total").val(promo4)
            }else if (elec == "promo4"){
                var promo4 = 600 
                $("#total").val(promo4)
            }

            
        }
    );

}
);
