def save_markdown(company_name, industry_info, company_info, use_cases, datasets):
    with open("output.md", "w") as f:
        f.write(f"# AI/ML/GenAI Use Cases for {Amazon}\n\n")
        f.write(f"## Industry Info\n{industry_info}\n\n")
        f.write(f"## Company Info\n{company_info}\n\n")
        f.write("## Use Cases\n")
        for case in use_cases:
            f.write(f"- {case}\n")
        
        f.write("\n## Dataset Resources\n")
        for case, link in datasets.items():
            f.write(f"- [{case}]({link})\n")

