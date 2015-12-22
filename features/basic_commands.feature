Feature: run the cli,
  type in text,
  exit the cli

  Scenario: run the cli, type something, exit
     Given the module "prompt_pptk" is installed
      when we run cli
      and we wait for prompt
      and we type in "boo"
      then we see "You entered: boo"
      when we send "ctrl + d"
      then cli exits
