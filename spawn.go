package main

import (
	"github.com/hagna/process"
	"fmt"
	"flag"
)

var chdir = flag.String("chdir", "", "change to this directory before spawning")


func main() {
	flag.Parse()
	o := make(chan *process.Message)
	done := make(chan bool, 1)
	args := flag.Args()
	go func() {
		for msg := range o {
			switch msg.Kind {
			case "stdout":
			case "stderr":
			case "end":
				fmt.Printf("%s:%d:%s,", msg.Kind, len(msg.Body), msg.Body)
			}
		}
		done <- true
	}()
	_ = process.StartProcess(*chdir, args, o)  //first arg is directory
	<-done
}
