<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Api extends CI_Controller{

    function __construct(){
        parent::__construct();
    }
    public function index(){
        echo 'teste';
    }
    public function requisicao(){
        $this->load->model("ReqModel");
        $method = $this->input->method(TRUE);
        //use get para consultas
        if($method=='GET'){
            $email=$this->input->get('email');
            $id=$this->input->get('id');
            $lista=[];
            if($email){
                $lista=$this->ReqModel->list($email,'email');
            }elseif($id){
                $lista=$this->ReqModel->list($id,'id');
            }else{
                $lista=$this->ReqModel->list();
            }
            echo json_encode($lista,JSON_PRETTY_PRINT);
        }
        //use post para cadastrar
        elseif($method=='POST'){
            $data= file_get_contents("php://input");
            $data=json_decode($data,TRUE);
            $this->ReqModel->add($data);
        }
        //use put para atualizar
        elseif ($method=="PUT") {
            $data= file_get_contents("php://input");
            $data=json_decode($data,TRUE);
            $this->ReqModel->update($data);
        }
        // use put e passe id via get para deletar
        elseif($method=='DELETE'){
            $id=$this->input->get('id');
            // $this->ReqModel->delete($id);
            $this->ReqModel->delete($id);
        }
    }



}
?>