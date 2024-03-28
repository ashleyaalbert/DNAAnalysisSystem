# 311-group-project



## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.bucknell.edu/kbw011/311-group-project.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.bucknell.edu/kbw011/311-group-project/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***


## DNA Analysis System
This project analyzes a DNA sequence against a DNA query to find similarities. The way these pieces of DNA are matched is up to the user! Choose between different algorithms, such as longest common subsequence or edit distance, to see the matches you get!

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

The DNA Analysis System allows for a user to analyze DNA sequences against a DNA query. The user will be welcomed and prompted to either enter their own files or use the current system's files. These files will be checked to ensure they are valid. The user will then be prompted to select an algorithm to go through the DNA. The possible options include Longest Common Substring, Longest Common Subsequence, Edit Distance, Needleman-Wunsch Algorithm, and Substring Alignment and Frequency Algorithm. The algorithm selected will then return a score and what DNA sequence best matches the DNA query. The user will then be prompted to continue by choosing another algorithm or quitting the system.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

One example of the use of this system is as follows:
If you opt to use the system files and select option 3, Edit Distance, the expected output will return:

All Scores:

SCORE: (0.5604472396925226) : NC_000011.10:c2161209-2159779 Homo sapiens chromosome 11, GRCh38.p13 Insulin


SCORE: (0.43986254295532645) : NT_176377.1:12394966-12397002 Guinea pig insulin gene


SCORE: (0.5191717791411044) : V00179.1 Dog gene encoding insulin


SCORE: (0.8071553228621291) : V01243.1 Rat gene for insulin 2


SCORE: (0.4817927170868347) : AY092023.1 Gorilla gorilla insulin gene, partial cds


SCORE: (0.4715219421101774) : NC_052536.1 Gallus gallus isolate bGalGal1 chromosome 5, Insulin


SCORE: (0.27472527472527475) : NC_045512.2:21563-25384 SARS-Cov-2 - surface spike protein


SCORE: (0.48351648351648346) : NC_002018.1:21-1385 Influenza A virus (A/Puerto Rico/8/1934(H1N1)) segment 6, neuraminidase 


SCORE: (0.455026455026455) : NC_007366.1:30-1730 Influenza A virus (A/New York/392/2004(H3N2)) segment 4, hemagglutinin    


SCORE: (0.4771241830065359) : MH537830.1 Streptococcus pyogenes strain SH2902A RopB-like (ropB) genes



MOST SIMILAR:
V01243.1 Rat gene for insulin 2


## Support
For support, email the authors at aaa016@bucknell.edu, cpe006@bucknell.edu, stv002@bucknell.edu, or kbw011@bucknell.edu.

## Contributing
We are currently not looking for contributions to the system, however, if you would like to suggest an improvement that can be made or algorithm that can be added, email one of the authors above.

## Authors and acknowledgment
Authors of this project include Ashley Albert, Charlie Ehrbar, Sam Vickers, and Katrina Wilson.

## License
This project is not licensed.

## Project Status and Roadmap
This project is currently complete, but open to adding new algorithms that can analyze DNA sequences and queries.
