def prompt_list_generator(prompt_list, company_name):
    updated_list = [prompt.replace("{company_type}", company_name) for prompt in prompt_list]
    return updated_list

# def prompt_list_generator(prompt_list, company_name, project_context):
#     updated_list = [add_context(prompt, company_name, project_context) for prompt in prompt_list]
#     return updated_list

# def add_context(prompt, company_name, project_context):
    
#     # Add contextual information to the prompt
	
#     context_inclusion = f"This is a website design project for {company_name}. {project_context}"
#     updated_prompt = prompt.replace("{company_type}", company_name).replace("{context_inclusion}", context_inclusion)
#     return updated_prompt
