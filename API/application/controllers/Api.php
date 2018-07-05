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
    public function resultado(){
        $this->load->model('ResultadoModel');
        $method = $this->input->method(TRUE);
        
    }
    public function salvar(){
    $file=fopen("logt.txt","w");
    fwrite($file,"entrou");
    $nome=$_POST['fileName'];
    // echo $nome;
    $arquivo = $_FILES['InputArquivo'];
        $configuracao = array(
        'upload_path'   => './files/',
        'allowed_types' => 'zip|',
        'file_name'     => $nome.'.zip',
        'max_size'      => '1000'
     );
     
     $this->load->library('upload');
     $this->upload->initialize($configuracao);
     if($this->upload->do_upload('InputArquivo')){
        // fwrite($file,"deu certo");
        $data=array(
            'matricula'=>$_POST['InputMatricula'],
            'email'=>$_POST['InputEmail'],
            'status'=>'espera',
            'arquivo'=>$nome.'.zip'
        );
        $this->load->model('reqModel');
        $this->reqModel->add($data);
     }else{
         fwrite($file,$this->upload->display_errors());
     }
    }



}
?>