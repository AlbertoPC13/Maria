# Maria

This project is a word suggestion microservice module developed for the Prototype tool to support the initial stage of learning to write in the Spanish language.

# Documentation

The word suggestion module consists of a Flask API that receives a text and returns a list of possible next words suggested by Google BERT model in his Spanish version. 

The API has a single endpoint that receives a GET request with a JSON body containing the text that will be concidered as context for the suggested word. The API returns a JSON with a list of suggested words.

## Creating a new branch

This project has a main branch and a development branch. To create a new branch, you have to run the following command:

```bash
git checkout -b <branch-name> origin
```

In this way, you will create a new branch from the origin branch.

> [!TIP]
> Remember to use the notation ***username/feature-name*** for the branch name.

On this branch, you can make the changes you need to make. Once you have finished, you have to add and commit the changes to the branch.

To add the changes, you have to run the following commands:

```bash
git add .
git commit -m "Commit message"
```

Or you can add and commit the changes in a single command:

```bash
git commit -am "Commit message"
```

To push the changes to the repository, you have to run the following command:

```bash
git push origin <branch-name>
```

This command will push the changes to the repository. 

> [!IMPORTANT]
> When the changes are pushed to the repository, you will create a new **remote branch**. You have to create a **pull request** to merge the changes into the **development branch**.

Once the changes are pushed, you can create a pull request to merge the changes into the development branch.

## Pull requests

This project has a main (***main***) branch and a development (***dev***) branch.

The development branch is used to deploy new features and changes to the project. The main branch is used to deploy the project to production.

### Development branch (***dev***)

The development branch is the branch where your local changes will be merged. 

> [!NOTE]
> The development branch doesn't require a pull request to merge the changes. However, it is **recommended to create a pull request** to keep track of the changes.

You can create a pull request on the Github website. To do this, you have to go to the repository and click on the ***Pull requests*** tab. Then, you have to click on the ***New pull request*** button.

Also, you can create a pull request by pressing the branch that you want to merge into the development branch and reviewing the changes you will see a button to create a pull request.

> [!CAUTION]
> When you create a pull request, you have to **select the development branch** as the base branch. The **main** branch comes by **default**, so you have to **change it to the development branch**.

### Main branch (***main***)

The main branch is the branch where the development branch is merged. This branch is used to deploy the project to production.

To merge the development branch into the main branch, you have to create a pull request. This pull request will be reviewed by the team and, once it is approved, the changes will be merged into the main branch.

> [!IMPORTANT]
> To get the branch merged, you have to comply the following checklist:
> - [x] The code is reviewed and approved by at least one team member.
> - [x] The code is tested and it doesn't break the project.
> - [x] All the comments and suggestions are addressed.
> - [x] The branches are up to date with the main branch.

After the pull request is approved, you can merge the changes into the main branch.

After the changes are merged into the main branch, the project will be deployed to production.

> [!NOTE]
> Once the changes are merged into the main branch, the development branch will be **updated** with the changes. This will happen **automatically** by the Github platform.

> [!WARNING]
> When the pull request is closed, the branch **must be deleted**. This is important to keep the repository clean and organized. The pull request will ask you if you want to **delete the branch after it is closed**.

## Testing

For testing purposes, you can run the Flask project on your local machine. There are two ways to do this: on linux or on Windows environment.

### Linux

To run the project on a Linux environment, you just need to run the ***localTest.sh*** file. This file will install the necessary dependencies and run the Flask project.

```bash
source localTest.sh
```
### Windows

To run the project on a Windows environment, you just need to run the ***localTest.ps1*** file. This file will install the necessary dependencies and run the Flask project.

```bash
.\localTest.ps1
```

### Deactivating the virtual environment

> [!IMPORTANT]
> The project requires a **virtual environment** to run. The script will create it, but you have to **deactivate it manually**.
>
> To deactivate the virtual environment, run the following command:
> ```bash
> deactivate
> ```
> **This command works for both Linux and Windows environments**.

> [!CAUTION]
> It is important to **deactivate the virtual** environment after running the project. If you don't do this, the virtual environment will keep running and it will consume your computer's resources.
