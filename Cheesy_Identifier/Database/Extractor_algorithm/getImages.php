<?php 

	include('simple_html_dom.php');

    function start_html(){
        echo "<html><head></head><body style=\"background-color: white; overflow-x: hidden;\"></body></html>";
    }

    function display_as_p($show, $size){
        echo "<p style=\"position: relative; display: inline-block; text-align: center; width: 100%; align: center; margin: 0 auto; color: green; font-size: $size;\">";
        echo $show."</p><br>";
    }

    $cheese_names = explode("_DL_", explode("_QF_", $_GET['link'])[0]);
    $feature_names = explode("_DL_", explode("_QF_", $_GET['link'])[1]);
    $clean = explode("_QF_", $_GET['link'])[2]."";
    $number_of_images = (int)(explode("_QF_", $_GET['link'])[3]."");
    $database_folder = explode("_QF_", $_GET['link'])[4]."\cheese_photos";

    if($clean === "yes"){
        foreach (glob($database_folder . '/*' , GLOB_ONLYDIR) as $files) { array_map('unlink', glob($files."/*.*")); }
        foreach (glob($database_folder.'/*')  as $dir_) { rmdir($dir_);   }
    }

    if (!file_exists($database_folder)) {  mkdir($database_folder, 0777, true); }

    for($i = 0; $i < sizeof($cheese_names); $i++){ $cheese_names[$i] = str_replace("_", " ", $cheese_names[$i]); }
    for($i = 0; $i < sizeof($feature_names); $i++){ $feature_names[$i] = str_replace("_", " ", $feature_names[$i]); }

    $permuted = [];

    for($i = 0; $i < sizeof($cheese_names); $i++){
        if(sizeof($feature_names) > 0){
            for($j = 0; $j < sizeof($feature_names); $j++){  array_push($permuted, [explode(" ", $cheese_names[$i])[0], $cheese_names[$i]." ".$feature_names[$j]]);  }
        }
        else{ array_push($permuted, [explode(" ", $cheese_names[$i])[0], $cheese_names[$i]]); }
    }

    foreach ($permuted as $key) {
        foreach ($key as $k => $value) {
           //echo $k." ".$value."<br>";
        }
    }

    start_html();

    display_as_p("<br>Extraction tool:", "250%");

    $title = implode(", ", $cheese_names);

    display_as_p("<br><br>Extracting following queries: $title.<br><br><br>", "180%");

    error_reporting(E_ERROR | E_PARSE);

    for($i = 0; $i < sizeof($permuted); $i++){

        $search_query = urlencode($permuted[$i][1]);

        $image_count = $number_of_images; $steps = 0; $k = 0; $l = 0;
        display_as_p($number_of_images."<br>","500%");
        do {
            
            $steps = $steps + 20;

            $html = file_get_html("https://www.google.com/search?q=$search_query&atb=v193-1&ia=web&tbm=isch&start=$steps");    
                
            //echo "https://www.google.com/search?q=$search_query&tbm=isch&start=$steps<br>";

            $images = $html->find('img');

            $root = str_replace(" ","_",$permuted[$i][0]);

            if (!file_exists($database_folder."/".$root)) { 
            
                mkdir($database_folder."/".$root, 0777, true);

                $fp = fopen($database_folder."/".$root."/label.txt","wb");
                fwrite($fp, $root);
                fclose($fp);

            }

            foreach($images as $image){

                $link = $image->getAttribute("src");

                if(strlen($link) > 5){

                	$arr_exclude_gif = explode(".",$link); $not_gif = true;  foreach($arr_exclude_gif as $ext){  if($ext == "gif"){ $not_gif = false; } }

                	if($not_gif){        		

        	        	$name = "image_".$l.".png";
        	        	#$ll = imagepng(imagecreatefromstring(file_get_contents($link)), $name);
        				file_put_contents($database_folder."/".$root."/".$name, file_get_contents($link));
        				$l++;

                	}

                }

            }

        } while($image_count >= $steps);

        unset($images);
        unset($html);
        
        $directory = str_replace("\\", "\\\\", $database_folder."\\".str_replace(" ","_",$permuted[$i][0])."\\");
        $filecount = 0; $files = glob($directory . "*");
        if ($files){ $filecount = count($files)-1; }

        display_as_p($filecount." photos of ".$permuted[$i][0]." were extracted and saved into ".$directory.".","140%;");

    }


?>
