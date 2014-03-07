<?php
echo "Killed!";
exec("sudo kill $(ps aux | grep .py | grep piglow | awk '{print $2}')");
?>
