terraform{
    required_providers {
      aws ={
          source = "aws"
          version=""
      }
    }
}

provider "aws" {
    credentials = file("somefile.json")
    project = ""
    region = ""
    zone = ""
  
}

resource "aws_vpc_network" "aws_vpc" {
    
}