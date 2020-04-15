<?php 


	include('simple_html_dom.php');
    

    
    
	$query = "parmesan cheese";  # MODIFICAR ESTA VARIÁVEL PARA EXTRAIR AS IMAGENS.




    $search_query = urlencode($query);
	
    $html = file_get_html( "https://www.google.com/search?q=$search_query&tbm=isch");    
    $images = $html->find('img');


    $image_count = 100; 
    $i = 0; 
    $k = 0;


    $root = str_replace(" ","_",$query);
    foreach($images as $image){

        if($i == $image_count) break;

        if (!file_exists('./'.$root)) { mkdir('./'.$root, 0777, true); }

        $i++;


        $link = $image->getAttribute("src");
        echo $link."<br>";

        if(strlen($link) > 5){

        	$arr_exclude_gif = explode(".",$link);

        	$not_gif = true;
        	foreach($arr_exclude_gif as $ext){  if($ext == "gif"){ $not_gif = false; } }

        	if($not_gif){        		

	        	$name = $root."_image_index_".$k.".png";
	        	#$ll = imagepng(imagecreatefromstring(file_get_contents($link)), $name);
				file_put_contents('./'.$root."/".$name, file_get_contents($link));
				$k++;

        	}

        }


        

    }


?>