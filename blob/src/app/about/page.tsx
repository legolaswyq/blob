'use client';

export default function About() {
  return (
    <div className="flex flex-col items-center">
      <section className="w-full py-12 md:py-24 lg:py-24 bg-white">
        <div className="container px-4 md:px-6 mx-auto">
          <div className="flex flex-col items-center space-y-8 text-center w-full">
            <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl">
              About Me
            </h1>
            <p className="mx-auto max-w-[900px] text-gray-500 md:text-xl">
              I am a passionate developer focused on building modern web applications using cutting-edge technologies.
            </p>
            <div className="w-full max-w-6xl mx-auto mt-8">
              <iframe
                src="/WalterWang2025.pdf"
                className="w-full h-[1000px] border-0"
                title="Walter Wang CV"
              />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
