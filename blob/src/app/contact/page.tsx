'use client';

export default function Contact() {
  const contactInfo = [
    {
      label: 'Email',
      value: 'Legolaswyq@gmail.com',
      href: 'mailto:Legolaswyq@gmail.com',
    },
    {
      label: 'Phone',
      value: '0221041307',
      href: 'tel:0221041307',
    },
    {
      label: 'LinkedIn',
      value: 'Yuqi Wang',
      href: 'https://www.linkedin.com/in/yuqi-wang-74a84b218/',
    },
  ];

  return (
    <div className="flex flex-col items-center">
      <section className="w-full py-12 md:py-24 lg:py-32 bg-white">
        <div className="container px-4 md:px-6 mx-auto">
          <div className="flex flex-col items-center space-y-8 text-center">
            <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl">
              Contact Me
            </h1>
            <p className="mx-auto max-w-[700px] text-gray-500 md:text-xl">
              Feel free to reach out through any of the following channels:
            </p>
            <div className="w-full max-w-md mx-auto mt-8">
              <div className="space-y-6">
                {contactInfo.map((info) => (
                  <div key={info.label} className="flex flex-col items-center p-6 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors">
                    <h2 className="text-lg font-semibold text-gray-900 mb-2">{info.label}</h2>
                    <a
                      href={info.href}
                      target={info.label === 'LinkedIn' ? '_blank' : undefined}
                      rel={info.label === 'LinkedIn' ? 'noopener noreferrer' : undefined}
                      className="text-blue-600 hover:text-blue-800 transition-colors"
                    >
                      {info.value}
                    </a>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
