<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class ResultadoModel extends CI_Model{

    function __construct(){
       parent::__construct();
  }

  public function add($dados){
    return $this->db->insert('resultado',$dados);
  }
  public function list($dado=NULL,$campo=NULL){  
    if($campo=='id_req'){
      return $this->db->query('select * from resultado where id_req='.$dado)->result();
    }else{
      return $this->db->query('select * from resultado')->result();
    }
  }
  public function update($data){
    if(isset($data['id'])){
      $this->db->where('id',$data['id']);
      $this->db->update('resultado',$data);
    }
  }
  public function delete($id){
    $this->db->where('id',$id);
    $this->db->delete('resultado');
  }








}