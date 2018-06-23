<?php
defined('BASEPATH') OR exit('No direct script access allowed');
// $route['default_controller'] = 'welcome';
// require_once ('../controllers/Api.php');
$route['default_controller'] = 'api';
$route['requisicao']='api/requisicao';
$route['404_override'] = '';
$route['translate_uri_dashes'] = FALSE;
