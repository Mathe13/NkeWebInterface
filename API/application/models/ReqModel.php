<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class ReqModel extends CI_Model{

    function __construct(){
       parent::__construct();
  }

  public function add($dados){
    return $this->db->insert('req',$dados);
  }
  public function list($dado=NULL,$campo=NULL){
    if($campo=='email'){
      return $this->db->query('select * from req where email="'.$dado.'"')->result();  
    }elseif($campo=='id'){
      return $this->db->query('select * from req where id='.$dado)->result();
    }else{
      return $this->db->query('select * from req')->result();
    }
  }
  public function update($data){
    if(isset($data['id'])){
      $this->db->where('id',$data['id']);
      $this->db->update('req',$data);
    }
  }
  public function delete($id){
    $this->db->where('id',$id);
    $this->db->delete('req');
  }








}