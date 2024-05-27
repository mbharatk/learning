! pip install transformers

# Load pipeline from transformers
from transformers import pipeline

# Load the summarization pipeline. Set facebook/bart-large-cnn as the model to use for summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# Your text to summarize
# Source: https://learn.microsoft.com/en-us/training/modules/intro-to-git/1-what-is-vc
text = """ Amazon has introduced a new Linux-based open-source operating system called Bottlerocket. 
The purpose of this OS is that it is specifically built to run containers. 
It runs in Amazon Elastic Kubernetes Service (EKS), Amazon Elastic Container Service (ECS). 
Bottlerocket is written primarily with memory-safe languages like Rust and Go. 
It mainly focuses on security and durability. Many containerized applications today are run 
on general-purpose operating systems that are updated package-by-package, 
which makes OS updates difficult to automate. To only run containers on a Linux system, 
a complete Linux distribution is not always necessary. Bottlerocket only includes essential 
software to run containers. Bottlerocket reduces the footprint of the underlying OS, aiding overall performance. 
Second, it limits the exposure to potential attacks, as many of the tools leveraged by would-be attackers aren’t there. 
Instead of a package update system, Bottlerocket uses a simple, image-based model that allows for a rapid & complete rollback if necessary. 
This removes opportunities for conflicts and breakage, making it easier for you to apply fleet-wide updates using orchestrators such as 
EKS confidently. Bottlerocket’s open development model enables customers and partners to produce custom builds, such as builds that support 
their preferred orchestrators. Changes in these custom builds can be added to the Bottlerocket open-source project.
Bottlerocket also uses a primarily read-only file system. Its integrity is checked at boot time via dm-verity. For additional security measures, 
SSH access is also discouraged and is only available through the admin container.
You can automate updates to Bottlerocket by using an orchestration service like Amazon EKS. Amazon also claims that including only the essential 
software to run containers reduces the attack surface compared to general-purpose Linux distributions.
"""

# Generate the summary
summary = summarizer(text, max_length=641, min_length=100)

# Print the summary
print(summary[0]['summary_text'])
print(summary)
