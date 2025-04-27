from research_agent import ResearchAgent
from use_case_agent import UseCaseAgent
from resource_agent import ResourceAgent
from utils import save_markdown

def main(company_name):
    research = ResearchAgent()
    industry_info, company_info = research.research(company_name)

    use_case_gen = UseCaseAgent()
    use_cases = use_case_gen.generate(industry_info)

    resource_collector = ResourceAgent()
    datasets = resource_collector.collect(use_cases)

    save_markdown(company_name, industry_info, company_info, use_cases, datasets)

if __name__ == "__main__":
    company_name = input("Enter Company/Industry Name: ")
    main(company_name)
