# docker-cpu-overload
Docker image for testing how your system reacts to extensive CPU utilization.

## Scope
I wanted simplicity, so there are no fine-grained controls. The container detects
the number of cores of your hardware and puts 100% CPU load on them until you
stop the container again.

## Disclaimer
Just make sure you know what you are doing. This image could damage your hardware
or increase your spend on Cloud Hosting.
